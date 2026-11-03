#include <stdio.h>

int main() {
    // 1. 声明变量
    float recharge_amount; // 充值金额 (使用float以支持带小数的金额)
    int points = 0;        // 奖励积分，初始化为0

    // 2. 提示用户输入
    printf("请输入一卡通充值金额: ");
    
    // 3. 读取用户输入
    scanf("%f", &recharge_amount);

    // 4. 判断金额是否大于等于1000
    if (recharge_amount >= 1000) {
        // 整数除法自带向下取整效果，例如 1250 / 100 = 12
        // 强制类型转换 (int) 防止将 float 赋值给 int 时产生警告
        points = (int)(recharge_amount / 100); 
        
        // 5. 按格式输出结果
        printf("本次充值可奖励%d积分\n", points);
    } else {
        // 如果小于1000，可以选择提示不满足条件，或者什么都不输出
        printf("充值金额未满1000元，不参与积分奖励活动。\n");
    }

    return 0;
}
