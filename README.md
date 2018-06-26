# gsnky
### 省农科院评价指标系统

使用：
* Django 2.0.6
* XAdmin 2.0.1
* MySQL 5.7


bugs:
* 产品下5种指标有一种不为空，则删除产品抛异常(应该是产品绑定了树深度为2的产品类型，又绑定了5种指标，导致删除时逻辑出错)。
* xadmin加入ueditor界面插件后自定义admin界面时，出错：'The model UserWidget is already registered', 使用 xadmin.site.unregister()无效。
* 加入ueditor界面的admin，时间控件失效。

