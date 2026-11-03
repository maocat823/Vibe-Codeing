#include <stdio.h>

int main() {
    // 1. 声明变量
    float a, b, c, max;

    // 2. 输入 abc
    printf("请输入三个实数（用空格隔开）: ");
    scanf("%f %f %f", &a, &b, &c);

    // 3. 第一次判断：a > b
    if (a > b) {
        max = a;
    } else {
        max = b;
    }

    // 4. 第二次判断：c > max
    if (c > max) {
        max = c;
    }

    // 5. 输出最大值
    // 注意：流程图里写的是 printf("%5.2f", max);
    // %5.2f 表示输出浮点数，保留两位小数，且占5个字符宽度
    printf("最大值为: %5.2f\n", max);

    return 0;
}
