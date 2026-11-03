#include <stdio.h>

int main() {
    // 1. 声明变量
    float credit; // 一卡通余额
    float salary; // 消费金额

    // 2. 提示用户输入
    printf("请输入一卡通余额与消费金额，用空格隔开: ");
    
    // 3. 读取用户输入
    scanf("%f %f", &credit, &salary);

    // 4. 判断：消费金额是否小于等于余额
    if (salary <= credit) { 
        // 如果消费金额 <= 余额，说明钱够
        printf("刷卡成功\n");
    } else {
        // 否则，说明钱不够
        printf("余额不足，请充值\n");
    }

    return 0;
}
