# 我的工具
我的工具主要包含自己积累的自动化工具，包括*Python爬虫*、*图片处理*等等。具体列表:

* generate file
	* generateFile
	* generateXML
	* generateStringXML
* generate drawables
	* generateAndroidDrawable (Java project)
	* generateDrawables (Python)
* generate ppt
	* autoGenerateAllPpt
	* generatePpt
* python utils
	* countLine
	* getPicture
	* one2multiLine  
***
##generate file
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
##generate drawables
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

并会在每一个文件夹(xxxhdpi大小和xxhdpi大小相同)下生成响应大小的`test.png`图片。
###generateDrawables(Python)

*尚未完成*
***
##generate ppt
生成ppt的工具
###generatePpt
**作用：**读取文件夹中的图片，并将不多于10张图片生成ppt，每张图片构成ppt的一页，并放在正中，高和宽小于等于ppt的高和宽。

**使用方法：**`generatePpt [imageDir] <pptFileName>` 默认将ppt保存在`Desktop/ppt`下。
###autoGenerateAllPpt
**作用：**自动获取某个文件夹下一级文件夹里面的所有图片，并将每个文件夹下的图片(不少于5张，不多于10张)做成一个ppt。
***
##python utils
使用Python做的一些小工具
### countLine
**作用：**输入文件夹和匹配文件名的字符串，递归的计算文件夹下所有匹配文件的行数，并输出到log文件中。

**使用方法：**`countLine <dir> <fileNameReg>`

###getPicture
**作用：**获取某些连接下的所有匹配`Target`和`regxs`的图片，并分别保存。

**使用方法：**需要自己修改文件中的一些参数。
***
联系方式：s18810577589@sina.com