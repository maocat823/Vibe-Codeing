#include <stdio.h>

//  分别输入 6 3、5 2、-8 0 

int main() {
	
	// 定义 a\b   定义和、差、商、积 sum,diff,prod,quot
	int a,b,sum,diff,quot;
	
	float prod;
	
	// 输入整数a,b
	scanf("%d %d",&a,&b);
	
	// 公式计算 a+b
	sum = a+b;
	diff = a-b;
	prod = (float)a/b;
	quot = a*b;
	
	// 输出 
	printf("%d %d %d \n",sum,diff,quot);
	printf("%f",prod);
	
	return 0;
}
