# coding: utf-8 
# 文本段落格式化处理
# 主要功能： 类似文件编辑器覆盖或填充特性的编程功能

# 文本内容
sample_text = '''The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

# textwrap 函数总结
# wrap(text,width=70,**kw) 输出一个list，每一行为list中的一个元素
# fill(text,width=70,**kw) 文本第一行缩进
# shorten(text,width,**kw) 摘要功能
# dedent(text) 移除缩进,空格
# indent(text,prefix,predicate=None)


# wrap
import textwrap
t1 = textwrap.wrap(sample_text) 
print(t1)

# fill
t2 = textwrap.fill(sample_text,initial_indent="*"*4)
print(t2)

# shorten
t3 = textwrap.shorten(sample_text,width=10)
print(t3) # The [...]

# dedent 
dedent_text = textwrap.dedent(sample_text)
print(dedent_text)

# indent
final = textwrap.indent(sample_text,'>')
print(final)


for width in [45,80]:
    print("{} Columns is : \n".format(width))
    t = textwrap.fill(sample_text,width=width)
    print(t)


t5 = textwrap.fill(sample_text,subsequent_indent="*")
print(t5)