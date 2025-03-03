#可以使用 pdf2docx 库来将 PDF 转换为 DOCX，具体步骤如下：

#安装依赖

pip install pdf2docx

Python 代码示例

from pdf2docx import Converter

# 输入 PDF 文件路径
pdf_path = "input.pdf"
# 输出 DOCX 文件路径
docx_path = "output.docx"

# 创建转换器对象
cv = Converter(pdf_path)
cv.convert(docx_path, start=0, end=None)  # 转换整个 PDF
cv.close()

print("转换完成！")

说明
	•	start=0, end=None：指定要转换的页码范围，None 表示转换到最后一页。
	•	cv.close()：转换完成后关闭文件，释放资源。

如果 PDF 复杂（如含大量图片、表格），转换效果可能需要手动调整。
