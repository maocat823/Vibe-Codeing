#include <stdio.h>

int main(){
	// 数据声明：定义整型变量s1，s2，s3，定义整形变量总分total，追高分max，最低分min，定义浮点型平均分avg
	int s1,s2,s3,total,max,min;
	float avg;
	// 输入s1,s2,s3
	scanf("%d %d %d",&s1,&s2,&s3);
	// total=s1+s2+s3
	total=s1+s2+s3;
	// avg=total/3.0
	avg=total/3.0;
	// 功能2：求最大值
	// max为 s1 s2 中最大值
	if(s1<s2){
		max=s2;
	} else{
		max=s1;
	}
	// max为s3和max里的最大值
	if(max<s3){
		max=s3;
	} 
	// 功能3：求最小值
	min=s1;
	if(min>s2){
		min=s2;
	} 
	if(min>s3){
		min=s3;
	}
	// 输出total，avg，max,min 
	printf("total=%d avg=%.2f max=%d min=%dn",total,avg,max,min);
	return 0; 
}
