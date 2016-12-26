## TagAttrDB

创建这个项目的主要原因是为了方便XSS Fuzz测试。
用于观察过滤器对于标签名和属性名的处理情况（黑名单or白名单or其他？）

----------

### tags

#### html_elements.txt

存放的都是去除了尖括号的html元素标签名

说明：
- `<!--...-->`和`<!DOCTYPE>`稍微特殊点，所以保留了尖括号（如果要保持格式统一，去掉尖括号就好了）
- 包括`svg`和`math`这两个比较特殊的html标签（尽管参考的资料文档都没把它们算在里面），但不包括它们专有的子标签，会在另外的文件里再专门给出（见svg_elements.txt 和 math_elements.txt）。在实际的漏洞测试中应该先确定是否能插入`svg`和`math`，再来测试它们的相关标签

参考来源：
- https://developer.mozilla.org/en/docs/Web/HTML/Element
- http://www.w3schools.com/tags/


#### svg_elements.txt

与svg相关的元素的标签名

参考来源：
- https://developer.mozilla.org/en-US/docs/Web/SVG

#### math_elements.txt

与math相关的元素的标签名

参考来源：
- https://developer.mozilla.org/en-US/docs/Web/MathML


----------

### attributes

#### global_attributes.txt


全局属性（global attributes）可以适用于任何html标签，甚至包括那些不属于html规范的标签

- `xml:lang`和`xml:base`来源于XHTML规范
- `data-xyz`是`data-*`这一系列属性的一个代表，`aria-xyz`是`aria-*`这一系列属性的代表
- event handler attributes也属于global attributes, 但是由于其较特殊，单独存放在另一个文件（见events文件夹）

参考来源：
- https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes
- https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset
- https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA

#### html_tag_attributes/*

html_tag_attributes文件夹里存放的是各个标签的专有属性（文件名对应标签名）。如果找不到以某标签为名的文件，说明此标签无专有属性

参考来源：
- https://developer.mozilla.org/en/docs/Web/HTML/Element
- https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes

#### svg_tag_attributes/*

svg_tag_attributes文件夹里存放的是svg相关元素各个标签的所有svg相关属性（文件名对应标签名）。如果找不到以某标签为名的文件，说明此标签文档不全（如mesh）或本身也是html标签（如video）

参考来源：
- https://developer.mozilla.org/en-US/docs/Web/SVG

#### math_tag_attributes/*

math_tag_attributes文件夹里存放的是math相关元素各个标签所有math相关属性（文件名对应标签名）。如果找不到以某标签为名的文件，说明此标签文档不全

参考来源：
- https://developer.mozilla.org/en-US/docs/Web/MathML

#### events/most_event_attributes.txt

事件属性

说明：
- 这个文件列举出了现有的绝大多数的事件属性（甚至包括一部分不能通过作为html标签属性来注册的事件和一部分尚没有明确给出文档的事件）
- 这个文件的用法：主要是用于绕过基于黑名单的过滤器。另外，它只是提供一些可能，比如你用它进行fuzz发现了一些绕过黑名单的事件属性但是你不清楚怎么用或到底能不能用，你应该去查找这个事件的相关文档资料
- 我想绝大多数情况下，这个文件应该是能满足fuzz的需求了，除非你需要的事件属性可能确实有点冷门

参考来源：
- https://developer.mozilla.org/en-US/docs/Web/Events
- https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes
- http://www.w3schools.com/TAgs/ref_eventattributes.asp
- http://www.htmlref.com/reference/appa/events1.htm
- http://brutelogic.com.br/webgun/
- https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers
- http://help.dottoro.com/ljfvvdnm.php

#### events/agnostic_event_attributes.txt

agnostic event handler attributes

说明：
- 这个文件列举出的事件属性是most_event_attributes.txt的一个子集，单独把它们列举出来的原因是这些事件属性可以在几乎任何html元素上触发（包括非标准的html元素）。方便在标签名被限制了的情况下进行fuzz
- `onblur`,`oncontextmenu`,`onfocus`,`oninput`,`onkeydown`,`onkeypress`,`onkeyup`,`onpaste`,这些需要搭配`contenteditable`属性使用
- 可能还没列举全，后续会再补充完善

参考来源：
- http://brutelogic.com.br/blog/agnostic-event-handlers/


----------

### 待补充完善：

- `aria-*`系列属性相关补充
- agnostic event handler attributes 补充完善
