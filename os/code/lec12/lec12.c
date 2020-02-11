#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>


int main(void){
	int fd;
	fd = open("date.txt", O_RDONLY);
	if(fd == -1){
		printf("Error : can not open file\n");
		return 1;
	}
	else{
		printf("FIle opened and now close_\n");
		close(fd);
		return 0;
	}
}

