# 我的工具
我的工具主要包含自己积累的自动化工具，包括*Python爬虫*、*图片处理*等等。具体列表:

* generate_file
	* generateFile
	* generateXML
	* generateStringXML
* generate_drawables
	* generateAndroidDrawable (Java project)
	* generateDrawables (Python)
	* batchGenerateDrawables （Python）
* generate_ppt
	* autoGenerateAllPpt
	* generatePpt
* python_utils
	* countLine
	* getPicture
	* one2multiLine  
	* argv_engine
	
***
##generate_file
主要是生成(字符型)文件的工具
###generateFile
**作用：**读取旧文件中的所有行，使用设置的字符(串)分割成两段，并在第一段的左边添加`left`，两段之间添加`middle`，第二段右边添加`right`，并保存到新文件中。

**使用方法：**`generate <file> <newFile> [splitRegularExpress] <left> <middle> <right>`，默认的分割字符(串)是`=`，并会忽略使用`#`开头的行。

**例子：** 

原始文件(file1)：

```
my name = Imdreaming
his name = Toby
#her name = Lucy
```
使用`generate file1 newFile Hey is .`生成新文件newFile:

```
Hey my name is Imdreaming.
Hey his name is Toby.
```
###generateXML
**作用：**作用和***generateFile***基本相同，生成的文件是具有xml格式的文件。

**使用方法：**`generateXML <file> <new file> [split regular express] <tag>`，默认的分割字符(串)是`=`，并会忽略使用`#`开头的行。

**例子：**

原始文件(file2)：

```
item1=Imdreaming
item2=Toby
#item3 = Lucy
```
使用`generateXML file2 newXml item`生成新文件newXml：

```
<item name="item1">Imdreaming</item>
<item name="item2">Toby</item>
```
###generateStringXML
**作用：**作用和***generateXML***基本相同，*tag*为`string`。

**使用方法：**`generateStringXML <file> <new file> [split regular express]`，默认的分割字符(串)是`=`，并会忽略使用`#`开头的行。

**例子：**

原始文件(file3)：

```
item1=Imdreaming
item2=Toby
#item3 = Lucy
```
使用`generateXML file3 newStringXml`生成新文件newStringXml：

```
<string name="item1">Imdreaming</string>
<string name="item2">Toby</string>
```
***
##generate_drawables
主要是生成Android drawable的工具
###generateAndroidDrawable (Java project)
**作用：**输入图片或包含图片的文件夹，将输入图片(或文件夹中每张图片)以Android xxhdpi(3倍)为基准进行缩放，并生成Android各种dpi下的图片。

**使用方法：**`bash generateAndroidDrawables.sh <srcFile|srcDir> <destDir>` 图片必须是png格式，文件夹中只有以`.png`结尾的文件才能缩放。

**例子：**

在`/Users/Imdreaming/Pictures`文件夹下有`test.png`文件，使用`bash generateAndroidDrawables.sh /Users/Imdreaming/Pictures/test.png /Users/Imdreaming/Pictures/res`将会在`/Users/Imdreaming/Pictures`目录下创建`res`目录，并生成多个文件夹，结构如下：

* drawable
* drawable-hdpi
* drawable-ldpi
* drawable-mdpi
* drawable-xhdpi
* drawable-xxhdpi
* drawable-xxxhdpi

并会在每一个文件夹(xxxhdpi大小和xxhdpi大小相同)下生成相应大小的`test.png`图片。
###generateDrawables(Python)

**作用：**输入图片，生成Android各种dpi下的图片。

**使用方法：**`python generateDrawable.py -p image_path -op out_path [-extra argv]` 

**参数说明：**

```
-p	:	图片路径，任意格式图片，非png图片将被转为png图片
-op	:	输出图片位置，若文件名不已drawable结尾，则会在此路径后新建drawable文件夹
extra:
		-on	:	输出图片名称，如果不设置，将使用原图名称
		-ms	:	输出图片最大大小，即在xxxdpi下的大小，若不设置，将使用原图大小
			格式:100-100
		-as	:	输出图片最大大小的缩放大小，若设置小于xxxdpi，则更大的缩放大小下图片不进行缩放
			可使用:	xxx | xx | x | h | m | l
			若不设置，默认使用'xxx'
		-is	:	能输出的最小缩放大小，若设置大于ldpi，则不会输出更小的缩放图片
			可使用:	xxx | xx | x | h | m | l
			若不设置，默认使用'l'
```

**例子：**

在`/Users/Imdreaming/Pictures`文件夹下有`test.png`文件，使用`python generateDrawable.py -p /Users/Imdreaming/Pictures/test.png -op /Users/Imdreaming/Pictures/res -as xx -is m`将会在`/Users/Imdreaming/Pictures`目录下创建`res`目录，并生成多个文件夹，结构如下：

* drawable-hdpi
* drawable-mdpi
* drawable-xhdpi
* drawable-xxhdpi	(原图大小)
* drawable-xxxhdpi	(原图大小)

并会在每一个文件夹下生成相应大小的`test.png`图片。
###batchGenerateDrawables （Python）
**作用：**批量生成Android各种dpi下的图片。

**使用方法：**`python batchGenerateDrawables.py <pic dir | pic file> <out dir> [-extra argv]`

**参数说明：**

```
<pic dir | pic file>	:	包含图片的目录或图片文件，任意格式图片，非png图片将被转为png图片
<out dir>				:	输出文件夹
extra:
	-ic	:	如果设置为true，说明需要生成的是launcher图片，输出图片的最大大小将被设置为 192-192
	-ms	:	输出图片最大大小，即在xxxdpi下的大小，若不设置，将使用原图大小
			格式:100-100
	-as	:	输出图片最大大小的缩放大小，若设置小于xxxdpi，则更大的缩放大小下图片不进行缩放
			可使用:	xxx | xx | x | h | m | l
			若不设置，默认使用'xxx'
	-is	:	能输出的最小缩放大小，若设置大于ldpi，则不会输出更小的缩放图片
			可使用:	xxx | xx | x | h | m | l
			若不设置，默认使用'l'
```

**例子：**在`/Users/Imdreaming/Pictures`文件夹下有`test1.png,test2.jpg`文件，使用`python batchGenerateDrawables.py /Users/Imdreaming/Pictures /Users/Imdreaming/Pictures/res -as xx -is m`将会在`/Users/Imdreaming/Pictures`目录下创建`res`目录，并生成多个文件夹，结构如下：

* drawable-hdpi
* drawable-mdpi
* drawable-xhdpi
* drawable-xxhdpi	(原图大小)
* drawable-xxxhdpi	(原图大小)

并会在每一个文件夹下生成相应大小的`test1.png`和`test2.png`图片。
***
##generate_ppt
生成ppt的工具
###generatePpt
**作用：**读取文件夹中的图片，并将不多于10张图片生成ppt，每张图片构成ppt的一页，并放在正中，高和宽小于等于ppt的高和宽。

**使用方法：**`generatePpt [imageDir] <pptFileName>` 默认将ppt保存在`Desktop/ppt`下。
###autoGenerateAllPpt
**作用：**自动获取某个文件夹下一级文件夹里面的所有图片，并将每个文件夹下的图片(不少于5张，不多于10张)做成一个ppt。
***
##python_utils
使用Python做的一些小工具
### countLine
**作用：**输入文件夹和匹配文件名的字符串，递归的计算文件夹下所有匹配文件的行数，并输出到log文件中。

**使用方法：**`countLine <dir> <fileNameReg>`

###getPicture
**作用：**获取某些连接下的所有匹配`Target`和`regxs`的图片，并分别保存。

**使用方法：**需要自己修改文件中的一些参数。
###argv_engine
内部有`process_argv(argv,keys,offset=-1)`函数，函数会根据`keys`来处理`sys.argv`数组并返回一个字典，字典中包含keys和sys.argv中对应的值，若`sys.argv`中没有对应值，`key`将不存在。函数中会判断`sys.argv`的长度是否大于`offset`，若不大于将返回`None`，在查找`key`时，若`key`在`sys.argv`中的位置小于等于`offset`，此`key`被忽略。
***
联系方式：s18810577589@sina.com