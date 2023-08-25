#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void dfs(int index);
bool mapIsValid(int index);

int index1,map[9][9];
bool allFinish;

int main(int argc, char* argv[]){
    bool algorithm =0;//输入 -d,algorithm=0,选择DFS，输入 -b,algorithm=1,选择BFS
    char *tmparr =(char*)malloc(64*sizeof(char));
    int *matrixin =(int*)malloc(81*sizeof(int));

    tmparr=argv[1];
    if(tmparr[1] =='b'){
        algorithm =1;
    }else{
        algorithm =0;
    }
    
    FILE *fp;
    if((fp=fopen(argv[2],"r"))==NULL)  //打开文件
    {
        printf("Can not open file!\n");
        exit(1);
    }
    for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
            fscanf(fp,"%d",&map[i][j]);
		}
	}
    index1 = 0;
	allFinish = false;
    if(algorithm==0) {

    dfs(0);
    }
    else if(algorithm==1){
        ;
    }
    
    
    return 0;
}


void dfs(int index1) {
	if (allFinish) {
		return;
	}
	if (index1 == 81) {
		allFinish = true;
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				char interval[2] = {0};	//(j % 3 == 2) ? {'\n','\0'} : {'\n', '\0'}
				interval[0] = (j % 9 == 8) ? '\n' : ' ';
				printf("%d%s", map[i][j], interval);
			}
		}
	}

	int x = index1 / 9, y = index1 % 9;
	if (map[x][y]) {
		dfs(index1 + 1);
	}
	else {
		// 对每个数字进行尝试
		for (int num = 1; num <= 9; num++) {
			// 判断当前行列有无该数字，以hasThisNum标志
			bool hasThisNum = false;
			for (int i = 0; i < 9; i++) {
				if (map[x][i] == num) {
					hasThisNum = true;
					break;
				}
			}
			if (!hasThisNum) {
				for (int i = 0; i < 9; i++) {
					if (map[i][y] == num) {
						hasThisNum = true;
						break;
					}
				}
			}

			// 若有则继续尝试下一数字，若无则填充后判断全局合法性
			if (hasThisNum) {
				continue;
			}
			else {
				map[x][y] = num;
				if (mapIsValid(index1)) {
					dfs(index1 + 1);
				}
				// 如果不合法，则将该位置重置为0后继续尝试下一数字
				map[x][y] = 0;
			}
		}
	}
}
/*
判断index所在3*3的块是否合法
*/


bool mapIsValid(int index1) {
	// x,y为当前块的左上角坐标
	int x = index1 / 9, y = index1 % 9;
	x -= (x%3);
	y -= (y%3);

	int count[10] = { 0 };
	for (int i=0; i < 3; i++) {
		for (int j=0; j < 3; j++) {
			count[map[x + i][y + j]]++;
			if (count[map[x + i][y + j]] > 1 && map[x + i][y + j]) {
				return false;
			}
		}
	}
	return true;
}












// // #include <stdio.h>
// // #include <stdlib.h>
// // #include <string.h>
// // #include <stdbool.h>

// // int main(int argc, char* argv[]){

// //     bool algorithm =0;
// //    // printf("algorithm= %d \n",algorithm);
// //    // printf("argc=%d\n",argc);
// //     for(int i =0;i<argc;i++){
// //         printf("argv[%d]=%s\n",i,argv[i]);
// //     }
    
// //     char *a =(char*)malloc(2*sizeof(char));
// //     a=argv[1];
// //     printf("!!!%c\n",a[1]);
// //     char set =a[1];
// //    // char bb ="b";
// //       printf("set=%c\n",set);
// //     //printf("bb=%c\n",bb);
// //     if(set =='b'){
// //         algorithm =1;
// //     }
// //     printf("algorithm= %d \n",algorithm);


// //     return 0;
// // }

// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// #include <stdbool.h>

// void dfs(int index);
// bool mapIsValid(int index);

// int index1,map[9][9];
// bool allFinish;

// int main(int argc, char* argv[]){
//     bool algorithm =0;//输入 -d,algorithm=0,选择DFS，输入 -b,algorithm=1,选择BFS
//     char *tmparr =(char*)malloc(64*sizeof(char));
//     int *matrixin =(int*)malloc(81*sizeof(int));
    
//     //for(int i =0;i<argc;i++){
//         //printf("argv[%d]=%s\n",i,argv[i]);
//     //}
    
//     tmparr=argv[1];
//     if(tmparr[1] =='b'){
//         algorithm =1;
//     }else{
//         algorithm =0;
//     }
//     //printf("algorithm= %d \n",algorithm);
    
//     FILE *fp;
//     if((fp=fopen(argv[2],"r"))==NULL)  //打开文件
//     {
//         printf("Can not open file!\n");
//         exit(1);
//     }
//     for(int i=0;i<81;i++){
//         fscanf(fp,"%d",&matrixin[i]);
//         //printf("%d ",matrixin[i]);
        
//         index1 = 0;
// 		allFinish = false;
// 		for (int i = 0; i < 9; i++) {
// 			for (int j = 0; j < 9; j++) {
//                 fscanf(fp,"%d",&map[i][j]);
// 				if (i==81) {
// 					return 0;
// 				}
// 			}
// 		}
// 		dfs(0);
        
//     }
    
    


    

    
    

//     return 0;
// }

// void dfs(int index1) {
// 	if (allFinish) {
// 		return;
// 	}
// 	if (index1 == 81) {
// 		allFinish = true;
// 		for (int i = 0; i < 9; i++) {
// 			for (int j = 0; j < 9; j++) {
// 				char interval[2] = {0};	//(j % 3 == 2) ? {'\n','\0'} : {'\n', '\0'}
// 				interval[0] = (j % 9 == 8) ? '\n' : ' ';
// 				printf("%d%s", map[i][j], interval);
// 			}
// 		}
// 	}

// 	int x = index1 / 9, y = index1 % 9;
// 	if (map[x][y]) {
// 		dfs(index1 + 1);
// 	}
// 	else {
// 		// 对每个数字进行尝试
// 		for (int num = 1; num <= 9; num++) {
// 			// 判断当前行列有无该数字，以hasThisNum标志
// 			bool hasThisNum = false;
// 			for (int i = 0; i < 9; i++) {
// 				if (map[x][i] == num) {
// 					hasThisNum = true;
// 					break;
// 				}
// 			}
// 			if (!hasThisNum) {
// 				for (int i = 0; i < 9; i++) {
// 					if (map[i][y] == num) {
// 						hasThisNum = true;
// 						break;
// 					}
// 				}
// 			}

// 			// 若有则继续尝试下一数字，若无则填充后判断全局合法性
// 			if (hasThisNum) {
// 				continue;
// 			}
// 			else {
// 				map[x][y] = num;
// 				if (mapIsValid(index1)) {
// 					dfs(index1 + 1);
// 				}
// 				// 如果不合法，则将该位置重置为0后继续尝试下一数字
// 				map[x][y] = 0;
// 			}
// 		}
// 	}
// }
// /*
// 判断index所在3*3的块是否合法
// */
// bool mapIsValid(int index1) {
// 	// x,y为当前块的左上角坐标
// 	int x = index1 / 9, y = index1 % 9;
// 	x -= (x%3);
// 	y -= (y%3);

// 	int count[10] = { 0 };
// 	for (int i=0; i < 3; i++) {
// 		for (int j=0; j < 3; j++) {
// 			count[map[x + i][y + j]]++;
// 			if (count[map[x + i][y + j]] > 1 && map[x + i][y + j]) {
// 				return false;
// 			}
// 		}
// 	}
// 	return true;
// }
