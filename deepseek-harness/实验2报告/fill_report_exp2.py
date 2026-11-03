# -*- coding: utf-8 -*-
"""填写“实验二-2026030503028-毛俊中.docx”的实验报告。"""
import io
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SRC = r"D:\Vibe-Codeing\deepseek-harness\实验二-2026030503028-毛俊中.docx"
OUT = r"D:\Vibe-Codeing\deepseek-harness\实验二-2026030503028-毛俊中-完成版.docx"
BASE = r"D:\Vibe-Codeing\deepseek-harness"

doc = Document(SRC)


def clear_cell(cell):
    tc = cell._tc
    for p in tc.findall(qn('w:p')):
        tc.remove(p)


def style_run(run, size=12, bold=False, ascii_font='Times New Roman', east='宋体'):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.name = ascii_font
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.insert(0, rFonts)
    rFonts.set(qn('w:ascii'), ascii_font)
    rFonts.set(qn('w:hAnsi'), ascii_font)
    rFonts.set(qn('w:eastAsia'), east)


def para(cell, text='', size=12, bold=False, align=None, line=21, sb=0, sa=0,
         ascii_font='Times New Roman', east='宋体'):
    p = cell.add_paragraph()
    pf = p.paragraph_format
    if line is not None:
        pf.line_spacing = Pt(line)
    pf.space_before = Pt(sb)
    pf.space_after = Pt(sa)
    if align is not None:
        p.alignment = align
    if text:
        r = p.add_run(text)
        style_run(r, size=size, bold=bold, ascii_font=ascii_font, east=east)
    return p


def image(cell, path, width_cm):
    p = cell.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.line_spacing = 1.0
    pf.space_before = Pt(4)
    pf.space_after = Pt(4)
    run = p.add_run()
    run.add_picture(path, width=Cm(width_cm))


def code_block(cell, code):
    lines = code.replace('\t', '    ').rstrip('\n').split('\n')
    for ln in lines:
        p = cell.add_paragraph()
        pf = p.paragraph_format
        pf.line_spacing = Pt(15)
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        if ln:
            r = p.add_run(ln)
            style_run(r, size=10.5, ascii_font='Courier New', east='宋体')


CODE1 = """#include <stdio.h>

int main() {
    int a, b, sum, diff, prod;
    float quot;

    printf("请输入两个整数：");
    scanf("%d %d", &a, &b);

    sum  = a + b;
    diff = a - b;
    prod = a * b;
    quot = (float)a / b;

    printf("和：%d\\n", sum);
    printf("差：%d\\n", diff);
    printf("积：%d\\n", prod);
    printf("商：%.2f\\n", quot);

    return 0;
}"""

CODE2 = """#include <stdio.h>
#define PI 3.14159

int main() {
    float r, area;

    printf("请输入圆的半径：");
    scanf("%f", &r);

    area = PI * r * r;

    printf("圆的面积为：%.2f\\n", area);

    return 0;
}"""

CODE3 = """#include <stdio.h>

int main() {
    int s1, s2, s3, total, max, min;
    float avg;

    printf("请输入3门课程的成绩：");
    scanf("%d %d %d", &s1, &s2, &s3);

    total = s1 + s2 + s3;
    avg = total / 3.0;

    max = s1;
    if (s2 > max) max = s2;
    if (s3 > max) max = s3;

    min = s1;
    if (s2 < min) min = s2;
    if (s3 < min) min = s3;

    printf("总分：%d\\n", total);
    printf("平均分：%.1f\\n", avg);
    printf("最高分：%d\\n", max);
    printf("最低分：%d\\n", min);

    return 0;
}"""

CODE4 = """#include <stdio.h>

int main() {
    int n;

    printf("请输入一个十进制整数：");
    scanf("%d", &n);

    printf("十进制：%d\\n", n);
    printf("八进制：%o\\n", n);
    printf("十六进制：%x\\n", n);

    return 0;
}"""


def task_block(cell, title, task_content, steps, test_text, principle, code, fc, con):
    para(cell, title, size=12, bold=True)
    para(cell, "1、任务分析", size=12, bold=True)
    para(cell, "（1）任务内容：" + task_content, size=12)
    para(cell, "（2）流程图：使用WPS绘制流程图，如下：", size=12)
    image(cell, fc, 11)
    para(cell, "2、具体步骤过程与结果截图", size=12, bold=True)
    para(cell, "（1）程序编写：", size=12)
    for s in steps:
        para(cell, s, size=12)
    para(cell, "（2）编译与测试：", size=12)
    para(cell, test_text, size=12)
    image(cell, con, 13)
    para(cell, "3、原理分析", size=12, bold=True)
    para(cell, principle, size=12)
    para(cell, "4、源码", size=12, bold=True)
    code_block(cell, code)


table = doc.tables[1]

# ---------- R3 实验内容 ----------
c3 = table.rows[3].cells[0]
clear_cell(c3)
para(c3, "三、实验（训）内容（原理、操作步骤等）", size=14, bold=True, line=21, sa=4)

task_block(
    c3,
    "（一）格式化输入2个整数，格式化输出这2个数的和、差、积、商",
    "从键盘输入2个整数a、b，计算并格式化输出这2个数的和、差、积、商。",
    [
        "① 包含头文件#include <stdio.h>，定义主函数main；",
        "② 定义整型变量a、b存放输入的两个整数，定义sum、diff、prod分别表示和、差、积，定义浮点型变量quot表示商；",
        "③ 使用printf函数提示用户输入两个整数，使用scanf函数以%d格式读取a、b的值；",
        "④ 分别计算sum=a+b、diff=a-b、prod=a*b、quot=(float)a/b；",
        "⑤ 使用printf函数分别输出和、差、积、商，其中商用%.2f保留两位小数。",
    ],
    "编译程序，错误和警告均为零；运行程序，分别输入6 3、5 2、-8 0进行测试，其中输入-8 0时因除数为0，商出现-inf异常，说明作除法前应判断除数是否为0。运行结果如下：",
    "本程序属于顺序结构，按“输入—计算—输出”的顺序逐条执行。利用scanf和printf完成数据的格式化输入与输出，利用算术运算符+、-、*、/完成和、差、积、商的计算。由于a、b均为整型，a/b执行的是整数除法，会舍去小数部分，所以在计算商时用(float)a/b把操作数强制转换为浮点型，再用%.2f输出，从而保留商的小数部分。输入“-8 0”时商为-inf，体现了除法运算中除数不能为0的边界问题。",
    CODE1,
    BASE + r"\flowcharts2\fc2_1.png",
    BASE + r"\console2\con2_1.png",
)

task_block(
    c3,
    "（二）编写圆面积计算器",
    "输入圆的半径r，根据公式S=πr²计算并输出圆的面积（保留2位小数）。",
    [
        "① 包含头文件#include <stdio.h>，用#define定义符号常量PI表示圆周率，定义主函数main；",
        "② 定义浮点型变量r表示半径、area表示面积；",
        "③ 使用printf函数提示用户输入半径，使用scanf函数以%f格式读取r的值；",
        "④ 根据公式area=PI*r*r计算圆的面积；",
        "⑤ 使用printf函数以%.2f格式输出面积。",
    ],
    "编译程序，错误和警告均为零；运行程序，分别输入1、2.5、0进行测试，输出结果与预期一致。运行结果如下：",
    "本程序为顺序结构，按“输入半径—计算面积—输出面积”的顺序执行。圆的面积公式为S=πr²，程序中用#define PI 3.14159定义圆周率，用area=PI*r*r完成面积计算。由于半径和面积都可能含有小数，因此r、area均定义为float类型，输入时用%f格式，输出时用%.2f保留两位小数，使结果准确、格式美观。",
    CODE2,
    BASE + r"\flowcharts2\fc2_2.png",
    BASE + r"\console2\con2_2.png",
)

task_block(
    c3,
    "（三）输入3门课程成绩（int），计算并输出：总分、平均分（保留1位小数）、最高分、最低分",
    "输入3门课程的成绩s1、s2、s3，计算并输出总分、平均分（保留1位小数）、最高分和最低分。",
    [
        "① 包含头文件#include <stdio.h>，定义主函数main；",
        "② 定义整型变量s1、s2、s3、total、max、min，定义浮点型变量avg；",
        "③ 使用printf函数提示输入3门成绩，使用scanf函数以%d格式读取s1、s2、s3；",
        "④ 计算总分total=s1+s2+s3，平均分avg=total/3.0；",
        "⑤ 以s1为初值，用if语句分别与s2、s3比较求出最高分max和最低分min；",
        "⑥ 使用printf函数输出总分、平均分（%.1f）、最高分和最低分。",
    ],
    "编译程序，错误和警告均为零；运行程序，分别输入80 90 100、60 60 60、55 66 44进行测试，计算结果均正确。运行结果如下：",
    "本程序以顺序结构为主，其中求最大值、最小值用简单的if单分支语句实现：先令max=s1、min=s1，再用s2、s3依次与max、min比较，若更大（或更小）则更新。平均分由total/3.0求得，由于3.0是浮点数，total/3.0执行的是浮点除法，结果保留小数部分，再用%.1f输出，满足保留1位小数的要求。",
    CODE3,
    BASE + r"\flowcharts2\fc2_3.png",
    BASE + r"\console2\con2_3.png",
)

task_block(
    c3,
    "（四）编写进制转换小工具，输入一个十进制整数用十进制、八进制、十六进制分别输出",
    "输入一个十进制整数n，分别以十进制、八进制、十六进制形式输出。",
    [
        "① 包含头文件#include <stdio.h>，定义主函数main；",
        "② 定义整型变量n存放输入的十进制整数；",
        "③ 使用printf函数提示用户输入一个十进制整数，使用scanf函数以%d格式读取n；",
        "④ 使用printf函数分别以%d、%o、%x格式输出n的十进制、八进制、十六进制形式。",
    ],
    "编译程序，错误和警告均为零；运行程序，输入0、255、-1进行测试，观察不同进制下数值的表示形式。运行结果如下：",
    "本程序属于顺序结构，关键在于printf函数的格式控制符：%d以十进制有符号整数输出，%o以八进制无符号整数输出，%x以十六进制小写无符号整数输出。同一个整数用不同的格式控制符输出，即可得到该数在不同进制下的表示。当输入负数时，%o和%x会按无符号数解析该整数的补码形式输出，因此得到较大的数。",
    CODE4,
    BASE + r"\flowcharts2\fc2_4.png",
    BASE + r"\console2\con2_4.png",
)

# ---------- R4 实验总结 ----------
c4 = table.rows[4].cells[0]
clear_cell(c4)
para(c4, "四、实验（训）总结（实验或实训结果分析、实验或实训中碰到的问题及解决方法、心得等）", size=14, bold=True, line=21, sa=4)
para(c4, "1.实验结果分析：", size=12, bold=True)
para(c4,
     "本次实验共完成四个顺序结构C程序，分别实现两个整数的和差积商、圆面积计算、三门课程成绩统计以及十进制到八进制、十六进制的转换。"
     "四个程序均按“输入—处理—输出”的顺序执行，编译时错误和警告为零，运行结果与预期一致。通过实验，熟悉了scanf和printf的格式化输入输出方法，"
     "掌握了int、float等数据类型的选用以及%d、%f、%.1f、%o、%x等格式控制符的使用，体会到顺序结构程序自上而下、逐条执行的特点。",
     size=12)
para(c4, "2.问题：", size=12, bold=True)
para(c4,
     "（1）两个整数相除时，若直接使用a/b，由于两个操作数都是整型，结果会舍去小数部分，导致商不准确；"
     "（2）输入“-8 0”这类含0除数的数据时，程序会出现-inf异常，说明程序缺少对除数为0的判断；"
     "（3）计算平均分时，若写成total/3（整数3），会丢失小数部分；"
     "（4）圆面积、平均分等需要保留小数时，容易把输出格式写错，如把%.2f写成%f或%d。",
     size=12)
para(c4, "3.解决方法及心得：", size=12, bold=True)
para(c4,
     "（1）计算商之前，将其中一个操作数强制转换为float，如(float)a/b，使除法按浮点运算进行；同时对除数是否为0进行判断，避免除零异常；"
     "（2）计算平均分时用total/3.0，利用浮点数3.0保证结果为浮点型；"
     "（3）根据数据类型选择合适的格式控制符：整型用%d，实型用%f，需要保留小数时用%.2f、%.1f，输出八进制、十六进制时分别用%o、%x；"
     "（4）编程前先画出流程图，理清输入、处理、输出三个环节，再动手编码，可以减少逻辑错误。"
     "通过本次实验，我进一步巩固了顺序结构程序的设计方法，认识到数据类型与格式控制符的匹配对结果正确性的重要影响，也提高了分析问题、调试程序的能力。",
     size=12)

doc.save(OUT)
print("saved", OUT)
