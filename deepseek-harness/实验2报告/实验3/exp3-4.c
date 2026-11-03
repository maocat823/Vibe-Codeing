#include <stdio.h>

int main() {
    // 1. 声明变量
    float weight; // 重量 (kg)
    float price;  // 单价 (元/kg)
    float amount;  // 消费总金额

    // 2. 提示并输入数据
    printf("请输入水果重量(kg)与单价(元)，用空格隔开: ");
    scanf("%f %f", &weight, &price);

    // 3. 多分支判断计算金额
    if (weight < 2) {
        // 小于2kg，不打折
        amount = weight * price;
    } 
    else if (weight >= 2 && weight < 5) {
        // 大于等于2kg小于5kg，打9折
        amount = weight * price * 0.9;
    } 
    else {
        // 大于等于5kg（即除了上面两种情况之外的情况），打8折
        amount = weight * price * 0.8;
    }

    // 4. 输出结果 (保留两位小数)
    printf("水果消费金额为: %.2f 元\n", amount);

    return 0;
}
