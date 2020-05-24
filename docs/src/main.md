<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.8.1" />
<title>src.main API documentation</title>
<meta name="description" content="" />
<link href='https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.0/normalize.min.css' rel='stylesheet'>
<link href='https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/8.0.0/sanitize.min.css' rel='stylesheet'>
<link href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/github.min.css" rel="stylesheet">
<style>.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
</head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>src.main</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def main():
    # instance = classes.InpGenerator(&#39;/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx&#39;,
    #                                   &#39;/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/stagnation_template.inp&#39;)
    # my_instance = graphs.Solution(&#39;/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/solutions&#39;)
    # graphy = graphs.Graph(&#39;X(cm)&#39;, &#39;Speed, U(cm/s)&#39;, &#39;My Title&#39;)
    # graphy.add_scatter_sol(my_instance, x=&#39;name2&#39;, y=&#39;H2O&#39;, colour=&#39;steelblue&#39;, X_value = 1.4995, best_fit_line= True)
    # # graphy.add_scatter_spreadsheet(&#39;/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.xlsx&#39;,
    # #                                x=&#39;mean_eqy&#39;, y=&#39;X_CO&#39;, colour=&#39;steelblue&#39;, filter_condition=&#39;mean_heaty&#39;,
    # #                                filter_value=0.6, y_error=&#39;delta_X_CO&#39;, legend=&#39;0.6&#39;, best_fit_line= True)
    # # graphy.add_scatter_spreadsheet(&#39;/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.xlsx&#39;,
    # #                                x=&#39;mean_eqy&#39;, y=&#39;X_CO&#39;, colour=&#39;red&#39;, filter_condition=&#39;mean_heaty&#39;,
    # #                                filter_value=0.3, y_error=&#39;delta_X_CO&#39;, legend=&#39;0.3&#39;, best_fit_line= True)
    # graphy.show_and_save(&#39;chemkin_launch_files/graphs&#39;, &#39;test&#39;)
    pass

if __name__ == &#34;__main__&#34;:
    main()</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="src.main.main"><code class="name flex">
<span>def <span class="ident">main</span></span>(<span>)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def main():
    # instance = classes.InpGenerator(&#39;/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx&#39;,
    #                                   &#39;/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/stagnation_template.inp&#39;)
    # my_instance = graphs.Solution(&#39;/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/solutions&#39;)
    # graphy = graphs.Graph(&#39;X(cm)&#39;, &#39;Speed, U(cm/s)&#39;, &#39;My Title&#39;)
    # graphy.add_scatter_sol(my_instance, x=&#39;name2&#39;, y=&#39;H2O&#39;, colour=&#39;steelblue&#39;, X_value = 1.4995, best_fit_line= True)
    # # graphy.add_scatter_spreadsheet(&#39;/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.xlsx&#39;,
    # #                                x=&#39;mean_eqy&#39;, y=&#39;X_CO&#39;, colour=&#39;steelblue&#39;, filter_condition=&#39;mean_heaty&#39;,
    # #                                filter_value=0.6, y_error=&#39;delta_X_CO&#39;, legend=&#39;0.6&#39;, best_fit_line= True)
    # # graphy.add_scatter_spreadsheet(&#39;/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.xlsx&#39;,
    # #                                x=&#39;mean_eqy&#39;, y=&#39;X_CO&#39;, colour=&#39;red&#39;, filter_condition=&#39;mean_heaty&#39;,
    # #                                filter_value=0.3, y_error=&#39;delta_X_CO&#39;, legend=&#39;0.3&#39;, best_fit_line= True)
    # graphy.show_and_save(&#39;chemkin_launch_files/graphs&#39;, &#39;test&#39;)
    pass</code></pre>
</details>
</dd>
</dl>
</section>
<section>
</section>
</article>
<nav id="sidebar">
<h1>Index</h1>
<div class="toc">
<ul></ul>
</div>
<ul id="index">
<li><h3>Super-module</h3>
<ul>
<li><code><a title="src" href="index.html">src</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="src.main.main" href="#src.main.main">main</a></code></li>
</ul>
</li>
</ul>
</nav>
</main>
<footer id="footer">
<p>Generated by <a href="https://pdoc3.github.io/pdoc"><cite>pdoc</cite> 0.8.1</a>.</p>
</footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
<script>hljs.initHighlightingOnLoad()</script>
</body>
</html>