from pyquery import PyQuery

fn = lambda: this.map(lambda i, el: PyQuery(this).outerHtml())
PyQuery.fn.listOuterHtml = fn
S = PyQuery(
'<ol>   <li>Coffee</li>   <li>Tea</li>   <li>Milk</li>   </ol>')
S('li').listOuterHtml()
