/*
 * Simple - REALLY simple memory mapping demonstration.
 *
 * Copyright (C) 2001 Alessandro Rubini and Jonathan Corbet
 * Copyright (C) 2001 O'Reilly & Associates
 *
 * The source code in this file can be freely used, adapted,
 * and redistributed in source or binary form, so long as an
 * acknowledgment appears in derived source files.  The citation
 * should list that the code comes from the book "Linux Device
 * Drivers" by Alessandro Rubini and Jonathan Corbet, published
 * by O'Reilly & Associates.   No warranty is attached;
 * we cannot take responsibility for errors or fitness for use.
 *
 * $Id: simple.c,v 1.12 2005/01/31 16:15:31 rubini Exp $
 */

#include <linux/module.h>
#include <linux/moduleparam.h>
#include <linux/init.h>
#include <asm/io.h>
#include <linux/kernel.h>   /* printk() */
#include <linux/slab.h>   /* kmalloc() */
#include <linux/vmalloc.h>
#include <linux/highmem.h>
#include <linux/fs.h>       /* everything... */
#include <linux/errno.h>    /* error codes */
#include <linux/types.h>    /* size_t */
#include <linux/mm.h>
#include <linux/kdev_t.h>
#include <asm/page.h>
#include <linux/cdev.h>

#include <linux/device.h>

static int simple_major = 0;
module_param(simple_major, int, 0);
MODULE_AUTHOR("Jonathan Corbet");
MODULE_LICENSE("Dual BSD/GPL");

/*
 * Open the device; in fact, there's nothing to do here.
 */
static int simple_open (struct inode *inode, struct file *filp)
{
	return 0;
}


/*
 * Closing is just as simpler.
 */
static int simple_release(struct inode *inode, struct file *filp)
{
	return 0;
}



/*
 * Common VMA ops.
 */
static void* pKKK0 = NULL;
static void* pKKK = NULL;

void simple_vma_alloc(void)
{
  int i;
  char *pC;

  if (pKKK0 != NULL) return;

  pKKK0 = kmalloc(0x2000, GFP_KERNEL); // no need to check pKKK0 = NULL; if NULL, map from physical memory 0 just like the original way
  pKKK = (void*)(((((unsigned long)pKKK0) + PAGE_SIZE -1) >> PAGE_SHIFT) << PAGE_SHIFT);

  pC = (char*)pKKK;
  if (pC == NULL) return;
  for(i=0;i<PAGE_SIZE;i+=4) { pC[i+0] = 'A'; pC[i+1] = 'B'; pC[i+2] = 'C'; pC[i+3] = 'D'; }
}

void simple_vma_open(struct vm_area_struct *vma)
{
        // no matter how long the user space application assign, the vm_end-vm_start shall be the multiple of PAGE_SIZE 
	printk(KERN_NOTICE "Simple VMA open, virt %lx %lx, phys %lx\n",
			vma->vm_start, vma->vm_end, vma->vm_pgoff << PAGE_SHIFT);
        printk(KERN_NOTICE "open = %p %p", pKKK0, pKKK);

#if 0
        unsigned char* pVma = __va(vma->vm_pgoff << PAGE_SHIFT);
        printk(KERN_NOTICE "data = %02x %02x %02x %02x", pVma[3], pVma[7], pVma[11], pVma[15]);
#endif
}

void simple_vma_close(struct vm_area_struct *vma)
{
	printk(KERN_NOTICE "Simple VMA close.\n");
}


/*
 * The remap_pfn_range version of mmap.  This one is heavily borrowed
 * from drivers/char/mem.c.
   ../misc-progs/mapper /dev/simpler 0x10000 0x10 | od -Ax -t x1
 */

static struct vm_operations_struct simple_remap_vm_ops = {
	.open =  simple_vma_open,
	.close = simple_vma_close,
};

static int simple_remap_mmap(struct file *filp, struct vm_area_struct *vma)
{
        printk(KERN_NOTICE "mmap = %p %p", pKKK0, pKKK);
        //printk(KERN_NOTICE "pgprot = %lx %lx %lx %lx", vma->vm_page_prot, pgprot_writecombine(vma->vm_page_prot), VM_IO, VM_RESERVED);
        vma->vm_page_prot = pgprot_writecombine(vma->vm_page_prot); // what's this function ??
	if (remap_pfn_range(vma, vma->vm_start, __pa(pKKK) >> PAGE_SHIFT /* vma->vm_pgoff */,
			    vma->vm_end - vma->vm_start,
			    vma->vm_page_prot))
		return -EAGAIN;

	vma->vm_ops = &simple_remap_vm_ops;
	simple_vma_open(vma);
	return 0;
}



/*
 * The nopage version.
 */
static int simple_vma_nopage(struct vm_area_struct *vma, struct vm_fault *vmf)
{
	struct page *pageptr;
	unsigned long offset = vma->vm_pgoff << PAGE_SHIFT;
	unsigned long physaddr = (unsigned long) vmf->virtual_address - vma->vm_start + offset;
	unsigned long pageframe = physaddr >> PAGE_SHIFT;

// Eventually remove these printks
	printk (KERN_NOTICE "---- Nopage, off %lx phys %lx nopage VA %p (%lx)\n", offset, physaddr, vmf->virtual_address, vma->vm_start);
	printk (KERN_NOTICE "VA is %p\n", __va (physaddr));
	printk (KERN_NOTICE "Page at %p\n", virt_to_page (__va (physaddr)));
	if (!pfn_valid(pageframe))
		return VM_FAULT_SIGBUS;
	pageptr = pfn_to_page(pageframe); // what's the mapping field ?
	printk (KERN_NOTICE "page->index = %ld mapping %p %p\n", pageptr->index, pageptr->mapping, page_address(pageptr));
	printk (KERN_NOTICE "Page frame %ld\n", pageframe);
	get_page(pageptr);
	vmf->page = pageptr;

	return 0;
}

static struct vm_operations_struct simple_nopage_vm_ops = {
	.open =   simple_vma_open,
	.close =  simple_vma_close,
	.fault = simple_vma_nopage,
};

static int simple_nopage_mmap(struct file *filp, struct vm_area_struct *vma)
{
	unsigned long offset = vma->vm_pgoff << PAGE_SHIFT;

	if (offset >= __pa(high_memory) || (filp->f_flags & O_SYNC))
		vma->vm_flags |= VM_IO;
	vma->vm_flags |= VM_RESERVED;

	vma->vm_ops = &simple_nopage_vm_ops;
	simple_vma_open(vma);
	return 0;
}

#define COPY_TO_USER_ARG(ArgUser, ArgKernel, type)		\
    if (copy_to_user((void __user *)ArgUser, &ArgKernel,	\
                     sizeof(type)))				\
    {								\
        return -EFAULT;						\
    }

#define COPY_FROM_USER_ARG(ArgUser, ArgKernel, type)		\
    if (copy_from_user(&ArgKernel, (void __user *)ArgUser,	\
                     sizeof(type)))				\
    {								\
        return -EFAULT;						\
    }

#define USER_SPACE_ACCESS_VALIDATE_ARG(arg, type)		\
    if (!access_ok(VERIFY_READ, (void __user *)arg,		\
                     sizeof(type)))				\
    {								\
        return -EFAULT;						\
    }

typedef struct IOMMU_USER_RANGE
{
        unsigned long start;  
        unsigned long size;
        unsigned long pageArray;  
        unsigned long nrPages;
}IOMMU_USER_RANGE_T;

int MMU_map_user_pages(IOMMU_USER_RANGE_T* prUserRange)
{
        int nr_pages;
        unsigned long first, last;
        struct page **pages;
        int res, j, write_flag;
        unsigned long uaddr, size;
        unsigned long start_chk_addr, end_chk_addr, addr;
 
        printk(KERN_ALERT "func: MMU_map_user_pages kick-off");

        write_flag = 1; // more ioctl command (set/get..) ???
        uaddr = prUserRange-> start;
        size = prUserRange->size;

        first = (uaddr & PAGE_MASK) >> PAGE_SHIFT;
        last = ((uaddr + size) & PAGE_MASK) >> PAGE_SHIFT;
        nr_pages = last - first + 1;
        if ((pages = kmalloc(nr_pages * sizeof(*pages), GFP_KERNEL)) == NULL)
        {
                return -ENOMEM;  
        }

        prUserRange->pageArray = (unsigned long)pages;

        /* Try to fault in all of the neccessary pages*/
        down_read(&current->mm->mmap_sem);
        /* rw == READ(0) means read from driver, user space write into memory area, otherwise write from driver if WRITE(1) and read from user space */
        res = get_user_pages(
                current,
                current->mm,
                uaddr,
                nr_pages, 
                write_flag, /* rw: 0=READ, 1=WRITE */
                0, /* don't force */
                pages,
                NULL);
        up_read(&current->mm->mmap_sem);

        prUserRange->nrPages = res;
        /* Errors and no page mapped should return here */
        if (res < nr_pages) goto out_unmap;
        
        /* checking the ptr directly */

        start_chk_addr = uaddr;
        end_chk_addr = uaddr + size;
        addr = start_chk_addr;
        j = 0; 

        while((addr >= start_chk_addr) && (addr <= end_chk_addr)) 
        {
                // if (CheckPTE(current->mm, addr) != TRUE)  // skip CheckPTE
                {
                        if (j < res && write_flag == 1)
                        {
                            char *pC = (char*)kmap(pages[j]); /* (char*)page_address(pages[j]); */ //( both is ok )
                            pC = pC + (uaddr - (first << PAGE_SHIFT));
                            if (pC != NULL)
                            {
                                pC[0] = 'P'; pC[1] = 'Q'; pC[2] = 'R'; pC[3] = 'S';
                                printk(KERN_ALERT "fill the pattern in virtual address=%p\n", pC);
                                kunmap(pages[j]);
                            }
                        }
                        if (j < res && write_flag == 0)
                        {
                            char *pC = (char*)kmap(pages[j]); /* (char*)page_address(pages[j]); */ //( both is ok )
                            pC = pC + (uaddr - (first << PAGE_SHIFT));
                            if (pC != NULL)
                            {
                                printk(KERN_ALERT "get data in virtual address=%p %02x %02x %02x %02x\n", pC, pC[0], pC[1], pC[2], pC[3]);
                                kunmap(pages[j]);
                            }
                        }
                        // printk(KERN_ALERT "check PTE at address 0x%x: fail\n", addr);
                        printk(KERN_ALERT "check PTE at address 0x%lx \n", addr);
                }
                addr += 0x1000; //PAGE_SIZE
                j++;
        }

        printk(KERN_ALERT "func: MMU_map_user_pages return 0x%x", nr_pages);
        return nr_pages;

out_unmap:
        printk(KERN_ALERT "get_user_pages fail\n");
        if (res > 0)
        {
                for(j=0; j<res; j++) put_page(pages[j]);
                res = 0;
        }
        kfree(pages);
        return res;
}

int MMU_unmap_user_pages(IOMMU_USER_RANGE_T* prUserRange)
{
        struct page **pages;
        int nr_pages, i;

        printk(KERN_ALERT "func: MMU_unmap_user_pages kick-off");
        pages = (struct page**) prUserRange->pageArray;
        nr_pages = prUserRange->nrPages;

        for (i=0; i< nr_pages; i++)
        {
               put_page(pages[i]);
        }   
     
        kfree(pages);
        return 0;
}

int MMU_user_map_ioctl(unsigned long arg)
{
        int res;
        IOMMU_USER_RANGE_T* prUserRange;
        IOMMU_USER_RANGE_T  rUserRange;

        prUserRange = (IOMMU_USER_RANGE_T*) arg;

        printk(KERN_ALERT "func: MMU_user_map_ioctl kick-off");
        USER_SPACE_ACCESS_VALIDATE_ARG(prUserRange, IOMMU_USER_RANGE_T);
        COPY_FROM_USER_ARG(prUserRange, rUserRange, IOMMU_USER_RANGE_T);

        res = MMU_map_user_pages(&rUserRange);

        COPY_TO_USER_ARG(prUserRange, rUserRange, IOMMU_USER_RANGE_T);

        return (res > 0) ? 0 : -EFAULT;
}

int MMU_user_unmap_ioctl(unsigned long arg)
{
        IOMMU_USER_RANGE_T* prUserRange;
        IOMMU_USER_RANGE_T  rUserRange;

        prUserRange = (IOMMU_USER_RANGE_T*) arg;

        printk(KERN_ALERT "func: MMU_user_unmap_ioctl kick-off");
        USER_SPACE_ACCESS_VALIDATE_ARG(prUserRange, IOMMU_USER_RANGE_T);
        COPY_FROM_USER_ARG(prUserRange, rUserRange, IOMMU_USER_RANGE_T);

        MMU_unmap_user_pages(&rUserRange);

        COPY_TO_USER_ARG(prUserRange, rUserRange, IOMMU_USER_RANGE_T);

        return 0;
}

/*
 * Ioctl definitions
 */

/* Use 'k' as magic number */ 
#define SIMPLE_IOC_MAGIC 'S'
/* Please use a different 8-bit number in your code */
#define SIMPLE_IOUSERMAP   _IO(SIMPLE_IOC_MAGIC,   0)
#define SIMPLE_IOUSERUNMAP _IO(SIMPLE_IOC_MAGIC,   1)
#define SIMPLE_IORESERVED1 _IOW(SIMPLE_IOC_MAGIC,  2, int) // ??
#define SIMPLE_IORESERVED2 _IOW(SIMPLE_IOC_MAGIC,  3, int) // ??
#define SIMPLE_IOC_MAXNR                           3

long simple_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)
{

        int err = 0;
        int retval = 0;

        printk(KERN_ALERT "simple_ioctl 0x%x 0x%x 0x%x 0x%x", cmd, _IOC_TYPE(cmd), _IOC_NR(cmd), _IOC_DIR(cmd));

        /*
         * extract the type and number bitfields, and don't decode
         * wrong cmds: return ENOTTY (inappropriate ioctl) before access_ok()
         */
        if (_IOC_TYPE(cmd) != SIMPLE_IOC_MAGIC) return -ENOTTY;
        if (_IOC_NR(cmd) > SIMPLE_IOC_MAXNR) return -ENOTTY;
    
        /* 
         * the direction is a bitmask, and VERIFY_WRITE catches R/W
         * transfers. 'Type' is user-oriented, while
         * access_ok is kernel-oriented, so the concept of "read" and 
         * "write" is reversed 
         */
        if (_IOC_DIR(cmd) & _IOC_READ)
                err = !access_ok(VERIFY_WRITE, (void __user *)arg, _IOC_SIZE(cmd));
        else if (_IOC_DIR(cmd) & _IOC_WRITE)
                err = !access_ok(VERIFY_READ, (void __user *)arg, _IOC_SIZE(cmd));
        if (err) return -EFAULT;

        switch(cmd) {
         
          case SIMPLE_IOUSERMAP:
                MMU_user_map_ioctl(arg);   
                break;

          case SIMPLE_IOUSERUNMAP:
                MMU_user_unmap_ioctl(arg);
                break;

          default: /* redundant, as cmd was checked against MAXNR */
                return -ENOTTY;
        }
        return retval;

}

/*
 * Set up the cdev structure for a device.
 */
static void simple_setup_cdev(struct cdev *dev, int minor,
		struct file_operations *fops)
{
	int err, devno = MKDEV(simple_major, minor);
    
	cdev_init(dev, fops);
	dev->owner = THIS_MODULE;
	dev->ops = fops;
	err = cdev_add (dev, devno, 1);
	/* Fail gracefully if need be */
	if (err)
		printk (KERN_NOTICE "Error %d adding simple%d", err, minor);
}


/*
 * Our various sub-devices.
 */
/* Device 0 uses remap_pfn_range */
static struct file_operations simple_remap_ops = {
	.owner   = THIS_MODULE,
	.open    = simple_open,
	.release = simple_release,
	.mmap    = simple_remap_mmap,
        .unlocked_ioctl = simple_ioctl,
};

/* Device 1 uses nopage */
static struct file_operations simple_nopage_ops = {
	.owner   = THIS_MODULE,
	.open    = simple_open,
	.release = simple_release,
	.mmap    = simple_nopage_mmap,
        .unlocked_ioctl = simple_ioctl,
};

#define MAX_SIMPLE_DEV 2

#if 0
static struct file_operations *simple_fops[MAX_SIMPLE_DEV] = {
	&simple_remap_ops,
	&simple_nopage_ops,
};
#endif

/*
 * We export two simple devices.  There's no need for us to maintain any
 * special housekeeping info, so we just deal with raw cdevs.
 */
static struct cdev SimpleDevs[MAX_SIMPLE_DEV];

/*
 * Module housekeeping.
 */
/*
find /usr/src/linux-headers-2.6.35-22-generic/include/linux -type f -exec grep -H "virt_to_phys(" {} \;
find /usr/src/linux-headers-2.6.35-22-generic/arch/x86/include/asm -type f -exec grep -H "virt_to_phys(" {} \;
what's /dev/mem usage :  /dev/mem provides access to system physical memory, not virtual. The kernels virtual address space can be accessed using /dev/kmem. 
#include < asm/io.h >
phys_addr = virt_to_phys(virt_addr);
virt_addr = phys_to_virt(phys_addr);
bus_addr = virt_to_bus(virt_addr);
virt_addr = bus_to_virt(bus_addr);
*/
static int simple_init(void)
{
	int result;
	dev_t dev = MKDEV(simple_major, 0);

	/* Figure out our device number. */
	if (simple_major)
		result = register_chrdev_region(dev, 2, "simple");
	else {
		result = alloc_chrdev_region(&dev, 0, 2, "simple");
		simple_major = MAJOR(dev);
	}
	if (result < 0) {
		printk(KERN_WARNING "simple: unable to get major %d\n", simple_major);
		return result;
	}
	if (simple_major == 0)
		simple_major = result;

	/* Now set up two cdevs. */
	simple_setup_cdev(SimpleDevs, 0, &simple_remap_ops);
	simple_setup_cdev(SimpleDevs + 1, 1, &simple_nopage_ops);

        simple_vma_alloc();

#if 0
        /* my test log */
        {
          // __pa(...) : logical to physical, __va(...) : physical to logical 
          // pfn_to_page(...): physical >> PAGE_SHIFT to page
          // virt_to_page(...): logical to page
          // kmap(...) : logical to virtual
          // virt_to_phys : seems not virtual to physical, seems logical to physical , the same as __pa
          void *kkk = kmalloc(1024, GFP_KERNEL);
          void *vvv = vmalloc(8192); // use vmalloc_to_page() ??
          void *vvvl = vvv; //high_memory + 0x120; //vvv; // it's virtual address but we use it as logical address w/o map
          struct page* pv = vmalloc_to_page(vvv);
          struct page* pvl = virt_to_page(vvvl);
          struct page* pl = virt_to_page(kkk);
          //void* kmm = kmap(pvl);
          //unsigned int pkmm = (unsigned int)virt_to_phys(kmm);

          printk(KERN_ALERT "high mem5 = %p %lx %p %p %p %p %p %lx %lx %lx %lx", high_memory, __pa(high_memory), __va(__pa(high_memory)), (void*)&simple_remap_ops, kkk, vvv, pv, page_to_phys(pv), page_to_phys(vmalloc_to_page(vvv + 4096)), VMALLOC_START, VMALLOC_END);
          printk(KERN_ALERT "page5 = %p %p %p %p %p", pvl, pl, page_address(pvl), page_address(pl), pfn_to_page(__pa(kkk) >> PAGE_SHIFT));
          //printk(KERN_ALERT "page4 = %p %p %p %p %p %p %lx %p %p", pvl, pl, page_address(pvl), page_address(pl), pfn_to_page(__pa(kkk) >> PAGE_SHIFT), kmm, pkmm, pfn_to_page(pkmm >> PAGE_SHIFT), 
          //                  virt_to_page(__va(pkmm)));
          //kunmap(pvl);
          kfree(kkk);
          vfree(vvv);
        }
#endif
	return 0;
}


static void simple_cleanup(void)
{
	cdev_del(SimpleDevs);
	cdev_del(SimpleDevs + 1);
	unregister_chrdev_region(MKDEV(simple_major, 0), 2);
        if (pKKK0) { kfree(pKKK0); pKKK0 = NULL; }
}


module_init(simple_init);
module_exit(simple_cleanup);
