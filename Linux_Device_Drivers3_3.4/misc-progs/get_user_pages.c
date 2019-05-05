/*
 * get_user_pages.c -- simple file that ioctl() with get_user_pages from user_pages to kernel space and prints it
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <errno.h>
#include <limits.h>

// the same as the IOCTL definition in simple.c

typedef struct IOMMU_USER_RANGE
{
        unsigned long start;  
        unsigned long size;
        unsigned long pageArray;  
        unsigned long nrPages;
}IOMMU_USER_RANGE_T;

/* Use 'k' as magic number */ 
#define SIMPLE_IOC_MAGIC 'S'
/* Please use a different 8-bit number in your code */
#define SIMPLE_IOUSERMAP   _IO(SIMPLE_IOC_MAGIC,   0)
#define SIMPLE_IOUSERUNMAP _IO(SIMPLE_IOC_MAGIC,   1)
#define SIMPLE_IORESERVED1 _IOW(SIMPLE_IOC_MAGIC,  2, int) // ??
#define SIMPLE_IORESERVED2 _IOW(SIMPLE_IOC_MAGIC,  3, int) // ??
#define SIMPLE_IOC_MAXNR                           3

int main(int argc, char **argv)
{
    char *fname;
    FILE *f;
    unsigned long len, i;
    char pattern;
    void* address;
    IOMMU_USER_RANGE_T rUserRange;

    if (argc !=4
       || sscanf(argv[2],"%c", &pattern) != 1
       || sscanf(argv[3],"%li", &len) != 1) {
        fprintf(stderr, "%s: Usage \"%s <file> <pattern> <len>\"\n", argv[0],
                argv[0]);
        exit(1);	
    }	    

    fname=argv[1];

    if (!(f=fopen(fname,"r"))) {
        fprintf(stderr, "%s: %s: %s\n", argv[0], fname, strerror(errno));
	exit(1);
    }

    address = malloc(len);

    if (address == NULL)
    {
        fprintf(stderr,"%s: malloc(): %s\n",argv[0], strerror(errno));
	exit(1);
    }

    for (i=0;i<len;i++) ((char*)address)[i] = pattern;
    rUserRange.start = (unsigned long)address;
    rUserRange.size = len;
    rUserRange.pageArray = 0;
    rUserRange.nrPages = 0;

    if (ioctl(fileno(f), SIMPLE_IOUSERMAP, &rUserRange) < 0)
    {
        fprintf(stderr,"%s: ioctl(SIMPLE_IOUSERMAP): %s\n",argv[0], strerror(errno));
	free(address);
	fclose(f);
	exit(1);
    }

    fprintf(stderr, "get_user_pages device = %s, addr = %p (length = %ld) for %ld pages\n",
            fname, address, len, rUserRange.nrPages);

    fwrite(address, 1, len, stdout);

    if (ioctl(fileno(f), SIMPLE_IOUSERUNMAP, &rUserRange) < 0)
    {
        fprintf(stderr,"%s: ioctl(SIMPLE_IOUSERUNMAP): %s\n",argv[0], strerror(errno));
	free(address);
	fclose(f);
	exit(1);
    }

    free(address);
    fclose(f);

    return 0;    
}

