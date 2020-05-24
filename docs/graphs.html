<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.8.1" />
<title>src.IO_files_creator.graphs API documentation</title>
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
<h1 class="title">Module <code>src.IO_files_creator.graphs</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">import pandas as pd
from os import listdir, path
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np

# set a global style for all graphs:
plt.style.use(&#39;seaborn-notebook&#39;)


class Solution():
    &#34;&#34;&#34;
    This takes a folder of .out files amnd converts them to a dictionary of pandas DataFrames.
    Create 2 new dataframe columns for name1 and name2 as additional filtering criteria.
    Write the names of failed runs to a file in the same folder called ERROR_RUNS.txt as these cannot be plotted.
    &#34;&#34;&#34;

    def __init__(self, path_to_solution_folder):
        self.sol = path_to_solution_folder

        # dictionary to store dataframes:
        self.df_dict = {}
        self.sol_to_df()

    def filter_txt(self, lines, add_X_col: bool = False):
        &#34;&#34;&#34;
        Use RegEx expression to find DataFrame col values and data and save them as two lists from .out file.
        :param lines: .out file formatted as &#39;/n&#39; seperated list of strings
        :param add_X_col: True adds an extra X(cm) column header.
        :return:
        &#34;&#34;&#34;
        col_list = []
        key_list = []
        col_tuple = [()]
        previous: str = &#34;&#34;
        row = []

        for line in enumerate(lines):
            if line[1].startswith(&#39;    1   &#39;):
                # get list of keys from row above the row starting with &#34;    1   &#34;
                new_key_list = re.findall(r&#34;\b[A-Z]{1}[\S]*&#34;, previous)
                if add_X_col == True:
                    new_key_list.insert(0, &#39;X(cm)&#39;)
                new_key_list.insert(0, &#34;Index&#34;)
                key_list = new_key_list

            # get list of columns from the row starting with &#34;    1   &#34; onwards until the next newline and format
            if not line[1].isspace():
                col_tuple = re.findall(r&#34;([-+]?[\d]+[\.]?[\d]*[E]?[-+]?[\d]+\b)|\s([\d]+)\s&#34;, line[1])
                if col_tuple != []:
                    row = [tup[0] or tup[1] for tup in col_tuple]
                    col_list.append(row)

            previous = line[1]

        return key_list, col_list

    def add_name_cols(self, out_file_name, df: pd.DataFrame):
        &#34;&#34;&#34;
        Add name1 and name2 columns to dataframe for filtering purposes. Use the actual name of the file to extract them.
        :param out_file_name: The name of solution .out file for processing
        :param df: The dataframe.
        :return:
        &#34;&#34;&#34;
        name = out_file_name.strip(&#34;.out&#34;)
        name1 = name.split(&#39;__&#39;)[0]
        name2 = name.split(&#39;__&#39;)[1]
        df[&#39;name1&#39;] = name1
        df[&#39;name2&#39;] = name2
        return df

    def sol_to_df(self):
        &#34;&#34;&#34;
        prints all failed files to a text file and transfers all other files to a DataFrame. Initialises an ERROR_RUNS.TXT file.
        Writes all file names with errors to these files instead of converting them to a DataFrame.
        :return:
        &#34;&#34;&#34;
        new_df = pd.DataFrame()

        # initalise an error file:
        txt_path = path.join(self.sol, &#34;ERROR_RUNS.txt&#34;)
        with open(txt_path, &#34;w&#34;) as error_file:
            error_file.write(&#34;The following files have errors and cannot be plotted: &#34;)

        # go through all .out files in solutions folder:
        for file in listdir(self.sol):
            if file.endswith(&#34;.out&#34;):
                full_path = path.join(self.sol, file)

                # readlines and if ERROR present in the file, write the name of file to error_file, otherwise create dataframe with data:
                with open(full_path, &#34;r&#34;) as f:
                    lines = f.readlines()
                    if any(&#34;ERROR&#34; in s for s in lines):
                        with open(txt_path, &#34;a&#34;) as error_file:
                            error_file.write(&#34;\n&#34; + file)
                    else:
                        whole_doc = &#39; &#39;.join(lines)
                        whole_doc = whole_doc.split(&#39; TWOPNT: &#39;, 1)[0]

                        # create new dataframe and a super new dataframe for every slice of data seperated by &#39;MOLE FRACTION&#39;
                        i = 0
                        filtered_lines = whole_doc.split(&#34;MOLE FRACTION&#34;)
                        for i in range(len(filtered_lines)):
                            split_filtered = filtered_lines[i].split(&#39;\n&#39;)

                            if i == 0:
                                key_list, col_list = self.filter_txt(split_filtered, add_X_col=False)
                                new_df = pd.DataFrame(col_list, columns=key_list)
                            else:
                                # merge all successive dataframes to inital dataframe on X(cm) as merge column:
                                key_list, col_list = self.filter_txt(split_filtered, add_X_col=True)
                                super_new_df = pd.DataFrame(col_list, columns=key_list)
                                super_new_df.drop(&#39;Index&#39;, axis=1, inplace=True)
                                new_df = new_df.merge(super_new_df, on=&#39;X(cm)&#39;)
                    name = file.strip(&#39;.out&#39;)
                    new_df = self.add_name_cols(file, new_df)
                    self.df_dict[name] = new_df


class Graph():
    def __init__(self, x_axis_label: str, y_axis_label: str, title: str, x_graph_size: int = 6,
                 y_graph_size: int = 6.5):
        &#34;&#34;&#34;
        Initialise a graph, based on object arguments. One figure is created per new graph object.
        Any data added will be plotted on same graph. Call the add_scatter() and add_line_of_best_fit() for every set of data you intend to plot.
        :param x_axis_label:
        :param y_axis_label:
        :param title: the title that will be set for the graph
        :param x_graph_size: default to almost square size 6 (increase number to change size ratio or increase resolution)
        :param y_graph_size: and default to almost square size 6.5 (increase number to change size ratio or increase resolution)
        &#34;&#34;&#34;
        self.fig = plt.figure(figsize=(x_graph_size, y_graph_size))

        # get access to axies functions:
        self.ax = self.fig.gca()

        # set format variables and format the figure:
        self.x_axis_label = x_axis_label
        self.y_axis_label = y_axis_label
        self.title = title

        self.add_format()
        self.set_grid_ticks()

    def add_format(self):
        &#34;&#34;&#34;
        Format graph. Add title, axies, tight layout, padding and grid.
        :return:
        &#34;&#34;&#34;
        # add title, names and layout:
        plt.title(self.title, pad=15, figure=self.fig)
        plt.xlabel(self.x_axis_label, figure=self.fig)
        plt.ylabel(self.y_axis_label, figure=self.fig)
        plt.tight_layout()

    def set_grid_ticks(self):
        &#34;&#34;&#34;
        sets maximum number of ticks and formats grid.
        :return:
        &#34;&#34;&#34;
        # set ticks based on a maximum number:
        self.ax.get_xaxis().set_major_locator(plticker.MaxNLocator(10, prune=None))
        self.ax.get_yaxis().set_major_locator(plticker.MaxNLocator(10, prune=None))
        self.ax.get_xaxis().set_minor_locator(plticker.MaxNLocator(50))
        self.ax.get_yaxis().set_minor_locator(plticker.MaxNLocator(50))

        #format ticks and rotate the labels:
        self.ax.grid(b=True, which=&#39;major&#39;, linestyle=&#39;-&#39;, linewidth=&#39;1.0&#39;, color=&#39;gainsboro&#39;, zorder=0,
                     figure=self.fig)
        self.ax.grid(b=True, which=&#39;minor&#39;, linestyle=&#39;:&#39;, linewidth=&#39;0.5&#39;, color=&#39;silver&#39;, zorder=0, figure=self.fig)

        plt.xticks(rotation=70)

    def add_scatter_spreadsheet(self, path_to_sheet: str, x: str, y: str, legend=&#34;&#34;, colour=&#39;darkgrey&#39;,
                                filter_condition=None,
                                filter_value=None, X_value: int = None, round_filter_to_dp: int = None,
                                y_error: str = None, error_colour=&#39;darkgray&#39;, best_fit_line: bool = False):
        &#34;&#34;&#34;
        Based on spreadsheet input (csv or excel), plot scatter plot on a figure belonging to the Graph() instance.
        Can be used to plot multiple datasets on the same graph
        :param path_to_sheet: full path as string including extension .csv or .xls*
        :param x: exact name of column in spreadsheet for the x data
        :param y: exact name of column in spreadsheet for the y data
        :param legend: legend label
        :param colour: of line and if selected, line of best fit
        :param filter_condition: name of spreadsheet column used as a filter for values
        :param filter_value: the value the filter_column should have for plotting data
        :param X_value: assumes filter condition is X(cm) and filter value is the X_value. For specialist spreadsheets only.
        :param round_filter_to_dp: rounds the filter column values to number of decimal places. Use negative values for 0s (nearest 10, 100 etc)
        :param y_error: column name for y error bars - if present will add error bars to plot
        :param error_colour: error bar colour
        :param best_fit_line: if True will add a line of best fit
        :return:
        &#34;&#34;&#34;
        # adding arguments globally to function so that they can be modified based on user input combination (e.g input type):
        my_filter_condition = filter_condition
        my_filter_value = filter_value
        data = pd.DataFrame()

        if X_value is not None:
            my_filter_condition = &#39;X(cm)&#39;
            my_filter_value = str(X_value)

        # if data input is an excel or csv spreadsheet:
        if &#39;xls&#39; in path_to_sheet:
            data = pd.read_excel(path_to_sheet, path_to_sheet=&#39;Sheet1&#39;)
        elif &#39;csv&#39; in path_to_sheet:
            data = pd.read_csv(path_to_sheet)

        if &#39;xls&#39; or &#39;csv&#39; in path_to_sheet:
            if round_filter_to_dp is not None:
                series = data[my_filter_condition]
                data[my_filter_condition] = series.round(decimals=round_filter_to_dp)
            if filter_condition is None:
                x_data = data[x]
                x_data = x_data.astype(&#39;float64&#39;)
                y_data = data[y]
                y_data = y_data.astype(&#39;float64&#39;)
            else:
                x_data = (data[x][(data[my_filter_condition] == my_filter_value)])
                x_data = x_data.astype(&#39;float64&#39;)
                y_data = (data[y][(data[my_filter_condition] == my_filter_value)])
                y_data = y_data.astype(&#39;float64&#39;)

        # for if an input is a dictionary of dataframes:
        plt.scatter(x_data, y_data, color=colour, zorder=10, s=20, label=legend, figure=self.fig)

        if legend != &#34;&#34;:
            plt.legend(loc=&#34;upper left&#34;)

        if y_error is not None and filter_condition is not None:
            error = (data[y_error][(data[my_filter_condition] == my_filter_value)])
            error = error.astype(&#39;float64&#39;)

            self.add_error_bar(x_data, y_data, error, error_colour)

        if best_fit_line is True:
            self.add_best_fit_line(x_data, y_data, colour = colour)

        elif y_error is not None and filter_condition is None:
            error = data[y_error]
            error = error.astype(&#39;float64&#39;)
            self.add_error_bar(x_data, y_data, error, error_colour)

    def add_scatter_sol(self, solution: Solution, x: str, y: str, name=&#34;&#34;, legend=&#34;&#34;, colour=&#39;darkgrey&#39;,
                        filter_condition=None,
                        filter_value=None, X_value: int = None, number_of_points=1, best_fit_line: bool= False):
        &#34;&#34;&#34;

        :param solution: name of instance when generating the data from the Solution() class (used for chemkin output folder data)
        :param x: exact name of column for the x data
        :param y: exact name of column for the y data
        :param name: if present, will search and plot data from a specific .out file. Must remove .out file extension - just write the file name
        :param legend: legend label
        :param colour: colour of line and if selected, line of best fit
        :param filter_condition: name of column used as a filter for values
        :param filter_value: the value the filter_column should have for plotting data
        :param X_value: assumes filter condition is X(cm) and filter value is the X_value.
        :param number_of_points: repressents n for plotting every nth point in the data. Use for very large datasets
        :param best_fit_line: if True will add a line of best fit
        :return:
        &#34;&#34;&#34;
        # input type is the name of a file/df stored in a dictionary:
        if name != &#34;&#34;:
            df = solution.df_dict.get(name, &#39;no such value&#39;)
            if &#39;no such value&#39; in df:
                raise IndexError(&#34;No file was found. Check the name doesn&#39;t contain a file extension&#34;)
            if filter_condition is None:
                x_data = df[x][(df.index % number_of_points == 1)]
                x_data = x_data.astype(&#39;float64&#39;)
                y_data = df[y][(df.index % number_of_points == 1)]
                y_data = y_data.astype(&#39;float64&#39;)
            else:
                x_data = (df[x][(df[filter_condition] == filter_value)])
                x_data = x_data.astype(&#39;float64&#39;)
                y_data = (df[y][(df[filter_condition] == filter_value)])
                y_data = y_data.astype(&#39;float64&#39;)
        elif name == &#34;&#34; and X_value != None:
            df_dict = solution.df_dict
            # for key, df in df_dict.items():
            df = pd.concat(df_dict)
            x_data = (df[x][(df[&#39;X(cm)&#39;] == str(X_value))])
            x_data = x_data.astype(&#39;float64&#39;)
            y_data = (df[y][(df[&#39;X(cm)&#39;] == str(X_value))])
            y_data = y_data.astype(&#39;float64&#39;)

        else:
            raise IndexError(&#34;Please input a filename or an X value&#34;)

        plt.scatter(x_data, y_data, color=colour, zorder=10, s=20, label=legend, figure=self.fig)
        if legend != &#34;&#34;:
            plt.legend(loc=&#34;upper left&#34;)

        if best_fit_line is True:
            self.add_best_fit_line(x_data, y_data, colour = colour)

    def add_best_fit_line(self, x, y, colour=None):
        &#34;&#34;&#34;
        converts x and y data to np.array, sorts in order of x, converts to dataframe, removes duplicate x values and plots a polyfit line.
        :param x: x data list/set/Series
        :param y: x data list/set/Series
        :param colour: colour of line
        :return:
        &#34;&#34;&#34;
        #convert data into numpy arrays:
        array_x, array_y = np.array(x), np.array(y)
        # sort x and y by x value
        order = np.argsort(array_x)
        xsort, ysort = array_x[order], array_y[order]

        #create a dataframe and add 2 columns for your x and y data:
        df = pd.DataFrame()
        df[&#39;xsort&#39;] = xsort
        df[&#39;ysort&#39;] = ysort
        #create new dataframe with no duplicate x values and corresponding mean values in all other cols:
        mean = df.groupby(&#39;xsort&#39;).mean()
        df_x = mean.index
        df_y = mean[&#39;ysort&#39;]
        # poly1d to create a polynomial line from coefficient inputs:
        trend = np.polyfit(df_x, df_y, 8)
        trendpoly = np.poly1d(trend)
        # plot polyfit line:
        plt.plot(df_x, trendpoly(df_x), linestyle=&#39;:&#39;, dashes=(6, 5), linewidth=&#39;0.8&#39;,
                     color=colour, zorder=9, figure=self.fig)

    def add_error_bar(self, x: str, y: str, y_error: str, colour):
        &#34;&#34;&#34;
        adds error bars
        :param self:
        :param x: x data as Series/list/array
        :param y: y data as Series/list/array
        :param y_error: y error data as Series/list/array
        :param colour: colour of error bars
        :return:
        &#34;&#34;&#34;
        plt.errorbar(x=x, y=y, yerr=y_error, fmt=&#39;none&#39;, color=colour, zorder=8,
                     figure=self.fig, elinewidth=1)

    def show_and_save(self, path_of_save_folder: str, name: str):
        &#34;&#34;&#34;
        shows and saves the figure - must be called to show the figure at the end of plotting
        :param self:
        :param path_of_save_folder: save figures to this folder
        :param name: save figures under this name
        :return:
        &#34;&#34;&#34;
        plt.show()
        plt.savefig(path_of_save_folder + name)</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="src.IO_files_creator.graphs.Graph"><code class="flex name class">
<span>class <span class="ident">Graph</span></span>
<span>(</span><span>x_axis_label: str, y_axis_label: str, title: str, x_graph_size: int = 6, y_graph_size: int = 6.5)</span>
</code></dt>
<dd>
<div class="desc"><p>Initialise a graph, based on object arguments. One figure is created per new graph object.
Any data added will be plotted on same graph. Call the add_scatter() and add_line_of_best_fit() for every set of data you intend to plot.
:param x_axis_label:
:param y_axis_label:
:param title: the title that will be set for the graph
:param x_graph_size: default to almost square size 6 (increase number to change size ratio or increase resolution)
:param y_graph_size: and default to almost square size 6.5 (increase number to change size ratio or increase resolution)</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class Graph():
    def __init__(self, x_axis_label: str, y_axis_label: str, title: str, x_graph_size: int = 6,
                 y_graph_size: int = 6.5):
        &#34;&#34;&#34;
        Initialise a graph, based on object arguments. One figure is created per new graph object.
        Any data added will be plotted on same graph. Call the add_scatter() and add_line_of_best_fit() for every set of data you intend to plot.
        :param x_axis_label:
        :param y_axis_label:
        :param title: the title that will be set for the graph
        :param x_graph_size: default to almost square size 6 (increase number to change size ratio or increase resolution)
        :param y_graph_size: and default to almost square size 6.5 (increase number to change size ratio or increase resolution)
        &#34;&#34;&#34;
        self.fig = plt.figure(figsize=(x_graph_size, y_graph_size))

        # get access to axies functions:
        self.ax = self.fig.gca()

        # set format variables and format the figure:
        self.x_axis_label = x_axis_label
        self.y_axis_label = y_axis_label
        self.title = title

        self.add_format()
        self.set_grid_ticks()

    def add_format(self):
        &#34;&#34;&#34;
        Format graph. Add title, axies, tight layout, padding and grid.
        :return:
        &#34;&#34;&#34;
        # add title, names and layout:
        plt.title(self.title, pad=15, figure=self.fig)
        plt.xlabel(self.x_axis_label, figure=self.fig)
        plt.ylabel(self.y_axis_label, figure=self.fig)
        plt.tight_layout()

    def set_grid_ticks(self):
        &#34;&#34;&#34;
        sets maximum number of ticks and formats grid.
        :return:
        &#34;&#34;&#34;
        # set ticks based on a maximum number:
        self.ax.get_xaxis().set_major_locator(plticker.MaxNLocator(10, prune=None))
        self.ax.get_yaxis().set_major_locator(plticker.MaxNLocator(10, prune=None))
        self.ax.get_xaxis().set_minor_locator(plticker.MaxNLocator(50))
        self.ax.get_yaxis().set_minor_locator(plticker.MaxNLocator(50))

        #format ticks and rotate the labels:
        self.ax.grid(b=True, which=&#39;major&#39;, linestyle=&#39;-&#39;, linewidth=&#39;1.0&#39;, color=&#39;gainsboro&#39;, zorder=0,
                     figure=self.fig)
        self.ax.grid(b=True, which=&#39;minor&#39;, linestyle=&#39;:&#39;, linewidth=&#39;0.5&#39;, color=&#39;silver&#39;, zorder=0, figure=self.fig)

        plt.xticks(rotation=70)

    def add_scatter_spreadsheet(self, path_to_sheet: str, x: str, y: str, legend=&#34;&#34;, colour=&#39;darkgrey&#39;,
                                filter_condition=None,
                                filter_value=None, X_value: int = None, round_filter_to_dp: int = None,
                                y_error: str = None, error_colour=&#39;darkgray&#39;, best_fit_line: bool = False):
        &#34;&#34;&#34;
        Based on spreadsheet input (csv or excel), plot scatter plot on a figure belonging to the Graph() instance.
        Can be used to plot multiple datasets on the same graph
        :param path_to_sheet: full path as string including extension .csv or .xls*
        :param x: exact name of column in spreadsheet for the x data
        :param y: exact name of column in spreadsheet for the y data
        :param legend: legend label
        :param colour: of line and if selected, line of best fit
        :param filter_condition: name of spreadsheet column used as a filter for values
        :param filter_value: the value the filter_column should have for plotting data
        :param X_value: assumes filter condition is X(cm) and filter value is the X_value. For specialist spreadsheets only.
        :param round_filter_to_dp: rounds the filter column values to number of decimal places. Use negative values for 0s (nearest 10, 100 etc)
        :param y_error: column name for y error bars - if present will add error bars to plot
        :param error_colour: error bar colour
        :param best_fit_line: if True will add a line of best fit
        :return:
        &#34;&#34;&#34;
        # adding arguments globally to function so that they can be modified based on user input combination (e.g input type):
        my_filter_condition = filter_condition
        my_filter_value = filter_value
        data = pd.DataFrame()

        if X_value is not None:
            my_filter_condition = &#39;X(cm)&#39;
            my_filter_value = str(X_value)

        # if data input is an excel or csv spreadsheet:
        if &#39;xls&#39; in path_to_sheet:
            data = pd.read_excel(path_to_sheet, path_to_sheet=&#39;Sheet1&#39;)
        elif &#39;csv&#39; in path_to_sheet:
            data = pd.read_csv(path_to_sheet)

        if &#39;xls&#39; or &#39;csv&#39; in path_to_sheet:
            if round_filter_to_dp is not None:
                series = data[my_filter_condition]
                data[my_filter_condition] = series.round(decimals=round_filter_to_dp)
            if filter_condition is None:
                x_data = data[x]
                x_data = x_data.astype(&#39;float64&#39;)
                y_data = data[y]
                y_data = y_data.astype(&#39;float64&#39;)
            else:
                x_data = (data[x][(data[my_filter_condition] == my_filter_value)])
                x_data = x_data.astype(&#39;float64&#39;)
                y_data = (data[y][(data[my_filter_condition] == my_filter_value)])
                y_data = y_data.astype(&#39;float64&#39;)

        # for if an input is a dictionary of dataframes:
        plt.scatter(x_data, y_data, color=colour, zorder=10, s=20, label=legend, figure=self.fig)

        if legend != &#34;&#34;:
            plt.legend(loc=&#34;upper left&#34;)

        if y_error is not None and filter_condition is not None:
            error = (data[y_error][(data[my_filter_condition] == my_filter_value)])
            error = error.astype(&#39;float64&#39;)

            self.add_error_bar(x_data, y_data, error, error_colour)

        if best_fit_line is True:
            self.add_best_fit_line(x_data, y_data, colour = colour)

        elif y_error is not None and filter_condition is None:
            error = data[y_error]
            error = error.astype(&#39;float64&#39;)
            self.add_error_bar(x_data, y_data, error, error_colour)

    def add_scatter_sol(self, solution: Solution, x: str, y: str, name=&#34;&#34;, legend=&#34;&#34;, colour=&#39;darkgrey&#39;,
                        filter_condition=None,
                        filter_value=None, X_value: int = None, number_of_points=1, best_fit_line: bool= False):
        &#34;&#34;&#34;

        :param solution: name of instance when generating the data from the Solution() class (used for chemkin output folder data)
        :param x: exact name of column for the x data
        :param y: exact name of column for the y data
        :param name: if present, will search and plot data from a specific .out file. Must remove .out file extension - just write the file name
        :param legend: legend label
        :param colour: colour of line and if selected, line of best fit
        :param filter_condition: name of column used as a filter for values
        :param filter_value: the value the filter_column should have for plotting data
        :param X_value: assumes filter condition is X(cm) and filter value is the X_value.
        :param number_of_points: repressents n for plotting every nth point in the data. Use for very large datasets
        :param best_fit_line: if True will add a line of best fit
        :return:
        &#34;&#34;&#34;
        # input type is the name of a file/df stored in a dictionary:
        if name != &#34;&#34;:
            df = solution.df_dict.get(name, &#39;no such value&#39;)
            if &#39;no such value&#39; in df:
                raise IndexError(&#34;No file was found. Check the name doesn&#39;t contain a file extension&#34;)
            if filter_condition is None:
                x_data = df[x][(df.index % number_of_points == 1)]
                x_data = x_data.astype(&#39;float64&#39;)
                y_data = df[y][(df.index % number_of_points == 1)]
                y_data = y_data.astype(&#39;float64&#39;)
            else:
                x_data = (df[x][(df[filter_condition] == filter_value)])
                x_data = x_data.astype(&#39;float64&#39;)
                y_data = (df[y][(df[filter_condition] == filter_value)])
                y_data = y_data.astype(&#39;float64&#39;)
        elif name == &#34;&#34; and X_value != None:
            df_dict = solution.df_dict
            # for key, df in df_dict.items():
            df = pd.concat(df_dict)
            x_data = (df[x][(df[&#39;X(cm)&#39;] == str(X_value))])
            x_data = x_data.astype(&#39;float64&#39;)
            y_data = (df[y][(df[&#39;X(cm)&#39;] == str(X_value))])
            y_data = y_data.astype(&#39;float64&#39;)

        else:
            raise IndexError(&#34;Please input a filename or an X value&#34;)

        plt.scatter(x_data, y_data, color=colour, zorder=10, s=20, label=legend, figure=self.fig)
        if legend != &#34;&#34;:
            plt.legend(loc=&#34;upper left&#34;)

        if best_fit_line is True:
            self.add_best_fit_line(x_data, y_data, colour = colour)

    def add_best_fit_line(self, x, y, colour=None):
        &#34;&#34;&#34;
        converts x and y data to np.array, sorts in order of x, converts to dataframe, removes duplicate x values and plots a polyfit line.
        :param x: x data list/set/Series
        :param y: x data list/set/Series
        :param colour: colour of line
        :return:
        &#34;&#34;&#34;
        #convert data into numpy arrays:
        array_x, array_y = np.array(x), np.array(y)
        # sort x and y by x value
        order = np.argsort(array_x)
        xsort, ysort = array_x[order], array_y[order]

        #create a dataframe and add 2 columns for your x and y data:
        df = pd.DataFrame()
        df[&#39;xsort&#39;] = xsort
        df[&#39;ysort&#39;] = ysort
        #create new dataframe with no duplicate x values and corresponding mean values in all other cols:
        mean = df.groupby(&#39;xsort&#39;).mean()
        df_x = mean.index
        df_y = mean[&#39;ysort&#39;]
        # poly1d to create a polynomial line from coefficient inputs:
        trend = np.polyfit(df_x, df_y, 8)
        trendpoly = np.poly1d(trend)
        # plot polyfit line:
        plt.plot(df_x, trendpoly(df_x), linestyle=&#39;:&#39;, dashes=(6, 5), linewidth=&#39;0.8&#39;,
                     color=colour, zorder=9, figure=self.fig)

    def add_error_bar(self, x: str, y: str, y_error: str, colour):
        &#34;&#34;&#34;
        adds error bars
        :param self:
        :param x: x data as Series/list/array
        :param y: y data as Series/list/array
        :param y_error: y error data as Series/list/array
        :param colour: colour of error bars
        :return:
        &#34;&#34;&#34;
        plt.errorbar(x=x, y=y, yerr=y_error, fmt=&#39;none&#39;, color=colour, zorder=8,
                     figure=self.fig, elinewidth=1)

    def show_and_save(self, path_of_save_folder: str, name: str):
        &#34;&#34;&#34;
        shows and saves the figure - must be called to show the figure at the end of plotting
        :param self:
        :param path_of_save_folder: save figures to this folder
        :param name: save figures under this name
        :return:
        &#34;&#34;&#34;
        plt.show()
        plt.savefig(path_of_save_folder + name)</code></pre>
</details>
<h3>Methods</h3>
<dl>
<dt id="src.IO_files_creator.graphs.Graph.add_best_fit_line"><code class="name flex">
<span>def <span class="ident">add_best_fit_line</span></span>(<span>self, x, y, colour=None)</span>
</code></dt>
<dd>
<div class="desc"><p>converts x and y data to np.array, sorts in order of x, converts to dataframe, removes duplicate x values and plots a polyfit line.
:param x: x data list/set/Series
:param y: x data list/set/Series
:param colour: colour of line
:return:</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def add_best_fit_line(self, x, y, colour=None):
    &#34;&#34;&#34;
    converts x and y data to np.array, sorts in order of x, converts to dataframe, removes duplicate x values and plots a polyfit line.
    :param x: x data list/set/Series
    :param y: x data list/set/Series
    :param colour: colour of line
    :return:
    &#34;&#34;&#34;
    #convert data into numpy arrays:
    array_x, array_y = np.array(x), np.array(y)
    # sort x and y by x value
    order = np.argsort(array_x)
    xsort, ysort = array_x[order], array_y[order]

    #create a dataframe and add 2 columns for your x and y data:
    df = pd.DataFrame()
    df[&#39;xsort&#39;] = xsort
    df[&#39;ysort&#39;] = ysort
    #create new dataframe with no duplicate x values and corresponding mean values in all other cols:
    mean = df.groupby(&#39;xsort&#39;).mean()
    df_x = mean.index
    df_y = mean[&#39;ysort&#39;]
    # poly1d to create a polynomial line from coefficient inputs:
    trend = np.polyfit(df_x, df_y, 8)
    trendpoly = np.poly1d(trend)
    # plot polyfit line:
    plt.plot(df_x, trendpoly(df_x), linestyle=&#39;:&#39;, dashes=(6, 5), linewidth=&#39;0.8&#39;,
                 color=colour, zorder=9, figure=self.fig)</code></pre>
</details>
</dd>
<dt id="src.IO_files_creator.graphs.Graph.add_error_bar"><code class="name flex">
<span>def <span class="ident">add_error_bar</span></span>(<span>self, x: str, y: str, y_error: str, colour)</span>
</code></dt>
<dd>
<div class="desc"><p>adds error bars
:param self:
:param x: x data as Series/list/array
:param y: y data as Series/list/array
:param y_error: y error data as Series/list/array
:param colour: colour of error bars
:return:</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def add_error_bar(self, x: str, y: str, y_error: str, colour):
    &#34;&#34;&#34;
    adds error bars
    :param self:
    :param x: x data as Series/list/array
    :param y: y data as Series/list/array
    :param y_error: y error data as Series/list/array
    :param colour: colour of error bars
    :return:
    &#34;&#34;&#34;
    plt.errorbar(x=x, y=y, yerr=y_error, fmt=&#39;none&#39;, color=colour, zorder=8,
                 figure=self.fig, elinewidth=1)</code></pre>
</details>
</dd>
<dt id="src.IO_files_creator.graphs.Graph.add_format"><code class="name flex">
<span>def <span class="ident">add_format</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><p>Format graph. Add title, axies, tight layout, padding and grid.
:return:</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def add_format(self):
    &#34;&#34;&#34;
    Format graph. Add title, axies, tight layout, padding and grid.
    :return:
    &#34;&#34;&#34;
    # add title, names and layout:
    plt.title(self.title, pad=15, figure=self.fig)
    plt.xlabel(self.x_axis_label, figure=self.fig)
    plt.ylabel(self.y_axis_label, figure=self.fig)
    plt.tight_layout()</code></pre>
</details>
</dd>
<dt id="src.IO_files_creator.graphs.Graph.add_scatter_sol"><code class="name flex">
<span>def <span class="ident">add_scatter_sol</span></span>(<span>self, solution: <a title="src.IO_files_creator.graphs.Solution" href="#src.IO_files_creator.graphs.Solution">Solution</a>, x: str, y: str, name='', legend='', colour='darkgrey', filter_condition=None, filter_value=None, X_value: int = None, number_of_points=1, best_fit_line: bool = False)</span>
</code></dt>
<dd>
<div class="desc"><p>:param solution: name of instance when generating the data from the Solution() class (used for chemkin output folder data)
:param x: exact name of column for the x data
:param y: exact name of column for the y data
:param name: if present, will search and plot data from a specific .out file. Must remove .out file extension - just write the file name
:param legend: legend label
:param colour: colour of line and if selected, line of best fit
:param filter_condition: name of column used as a filter for values
:param filter_value: the value the filter_column should have for plotting data
:param X_value: assumes filter condition is X(cm) and filter value is the X_value.
:param number_of_points: repressents n for plotting every nth point in the data. Use for very large datasets
:param best_fit_line: if True will add a line of best fit
:return:</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def add_scatter_sol(self, solution: Solution, x: str, y: str, name=&#34;&#34;, legend=&#34;&#34;, colour=&#39;darkgrey&#39;,
                    filter_condition=None,
                    filter_value=None, X_value: int = None, number_of_points=1, best_fit_line: bool= False):
    &#34;&#34;&#34;

    :param solution: name of instance when generating the data from the Solution() class (used for chemkin output folder data)
    :param x: exact name of column for the x data
    :param y: exact name of column for the y data
    :param name: if present, will search and plot data from a specific .out file. Must remove .out file extension - just write the file name
    :param legend: legend label
    :param colour: colour of line and if selected, line of best fit
    :param filter_condition: name of column used as a filter for values
    :param filter_value: the value the filter_column should have for plotting data
    :param X_value: assumes filter condition is X(cm) and filter value is the X_value.
    :param number_of_points: repressents n for plotting every nth point in the data. Use for very large datasets
    :param best_fit_line: if True will add a line of best fit
    :return:
    &#34;&#34;&#34;
    # input type is the name of a file/df stored in a dictionary:
    if name != &#34;&#34;:
        df = solution.df_dict.get(name, &#39;no such value&#39;)
        if &#39;no such value&#39; in df:
            raise IndexError(&#34;No file was found. Check the name doesn&#39;t contain a file extension&#34;)
        if filter_condition is None:
            x_data = df[x][(df.index % number_of_points == 1)]
            x_data = x_data.astype(&#39;float64&#39;)
            y_data = df[y][(df.index % number_of_points == 1)]
            y_data = y_data.astype(&#39;float64&#39;)
        else:
            x_data = (df[x][(df[filter_condition] == filter_value)])
            x_data = x_data.astype(&#39;float64&#39;)
            y_data = (df[y][(df[filter_condition] == filter_value)])
            y_data = y_data.astype(&#39;float64&#39;)
    elif name == &#34;&#34; and X_value != None:
        df_dict = solution.df_dict
        # for key, df in df_dict.items():
        df = pd.concat(df_dict)
        x_data = (df[x][(df[&#39;X(cm)&#39;] == str(X_value))])
        x_data = x_data.astype(&#39;float64&#39;)
        y_data = (df[y][(df[&#39;X(cm)&#39;] == str(X_value))])
        y_data = y_data.astype(&#39;float64&#39;)

    else:
        raise IndexError(&#34;Please input a filename or an X value&#34;)

    plt.scatter(x_data, y_data, color=colour, zorder=10, s=20, label=legend, figure=self.fig)
    if legend != &#34;&#34;:
        plt.legend(loc=&#34;upper left&#34;)

    if best_fit_line is True:
        self.add_best_fit_line(x_data, y_data, colour = colour)</code></pre>
</details>
</dd>
<dt id="src.IO_files_creator.graphs.Graph.add_scatter_spreadsheet"><code class="name flex">
<span>def <span class="ident">add_scatter_spreadsheet</span></span>(<span>self, path_to_sheet: str, x: str, y: str, legend='', colour='darkgrey', filter_condition=None, filter_value=None, X_value: int = None, round_filter_to_dp: int = None, y_error: str = None, error_colour='darkgray', best_fit_line: bool = False)</span>
</code></dt>
<dd>
<div class="desc"><p>Based on spreadsheet input (csv or excel), plot scatter plot on a figure belonging to the Graph() instance.
Can be used to plot multiple datasets on the same graph
:param path_to_sheet: full path as string including extension .csv or .xls*
:param x: exact name of column in spreadsheet for the x data
:param y: exact name of column in spreadsheet for the y data
:param legend: legend label
:param colour: of line and if selected, line of best fit
:param filter_condition: name of spreadsheet column used as a filter for values
:param filter_value: the value the filter_column should have for plotting data
:param X_value: assumes filter condition is X(cm) and filter value is the X_value. For specialist spreadsheets only.
:param round_filter_to_dp: rounds the filter column values to number of decimal places. Use negative values for 0s (nearest 10, 100 etc)
:param y_error: column name for y error bars - if present will add error bars to plot
:param error_colour: error bar colour
:param best_fit_line: if True will add a line of best fit
:return:</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def add_scatter_spreadsheet(self, path_to_sheet: str, x: str, y: str, legend=&#34;&#34;, colour=&#39;darkgrey&#39;,
                            filter_condition=None,
                            filter_value=None, X_value: int = None, round_filter_to_dp: int = None,
                            y_error: str = None, error_colour=&#39;darkgray&#39;, best_fit_line: bool = False):
    &#34;&#34;&#34;
    Based on spreadsheet input (csv or excel), plot scatter plot on a figure belonging to the Graph() instance.
    Can be used to plot multiple datasets on the same graph
    :param path_to_sheet: full path as string including extension .csv or .xls*
    :param x: exact name of column in spreadsheet for the x data
    :param y: exact name of column in spreadsheet for the y data
    :param legend: legend label
    :param colour: of line and if selected, line of best fit
    :param filter_condition: name of spreadsheet column used as a filter for values
    :param filter_value: the value the filter_column should have for plotting data
    :param X_value: assumes filter condition is X(cm) and filter value is the X_value. For specialist spreadsheets only.
    :param round_filter_to_dp: rounds the filter column values to number of decimal places. Use negative values for 0s (nearest 10, 100 etc)
    :param y_error: column name for y error bars - if present will add error bars to plot
    :param error_colour: error bar colour
    :param best_fit_line: if True will add a line of best fit
    :return:
    &#34;&#34;&#34;
    # adding arguments globally to function so that they can be modified based on user input combination (e.g input type):
    my_filter_condition = filter_condition
    my_filter_value = filter_value
    data = pd.DataFrame()

    if X_value is not None:
        my_filter_condition = &#39;X(cm)&#39;
        my_filter_value = str(X_value)

    # if data input is an excel or csv spreadsheet:
    if &#39;xls&#39; in path_to_sheet:
        data = pd.read_excel(path_to_sheet, path_to_sheet=&#39;Sheet1&#39;)
    elif &#39;csv&#39; in path_to_sheet:
        data = pd.read_csv(path_to_sheet)

    if &#39;xls&#39; or &#39;csv&#39; in path_to_sheet:
        if round_filter_to_dp is not None:
            series = data[my_filter_condition]
            data[my_filter_condition] = series.round(decimals=round_filter_to_dp)
        if filter_condition is None:
            x_data = data[x]
            x_data = x_data.astype(&#39;float64&#39;)
            y_data = data[y]
            y_data = y_data.astype(&#39;float64&#39;)
        else:
            x_data = (data[x][(data[my_filter_condition] == my_filter_value)])
            x_data = x_data.astype(&#39;float64&#39;)
            y_data = (data[y][(data[my_filter_condition] == my_filter_value)])
            y_data = y_data.astype(&#39;float64&#39;)

    # for if an input is a dictionary of dataframes:
    plt.scatter(x_data, y_data, color=colour, zorder=10, s=20, label=legend, figure=self.fig)

    if legend != &#34;&#34;:
        plt.legend(loc=&#34;upper left&#34;)

    if y_error is not None and filter_condition is not None:
        error = (data[y_error][(data[my_filter_condition] == my_filter_value)])
        error = error.astype(&#39;float64&#39;)

        self.add_error_bar(x_data, y_data, error, error_colour)

    if best_fit_line is True:
        self.add_best_fit_line(x_data, y_data, colour = colour)

    elif y_error is not None and filter_condition is None:
        error = data[y_error]
        error = error.astype(&#39;float64&#39;)
        self.add_error_bar(x_data, y_data, error, error_colour)</code></pre>
</details>
</dd>
<dt id="src.IO_files_creator.graphs.Graph.set_grid_ticks"><code class="name flex">
<span>def <span class="ident">set_grid_ticks</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><p>sets maximum number of ticks and formats grid.
:return:</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def set_grid_ticks(self):
    &#34;&#34;&#34;
    sets maximum number of ticks and formats grid.
    :return:
    &#34;&#34;&#34;
    # set ticks based on a maximum number:
    self.ax.get_xaxis().set_major_locator(plticker.MaxNLocator(10, prune=None))
    self.ax.get_yaxis().set_major_locator(plticker.MaxNLocator(10, prune=None))
    self.ax.get_xaxis().set_minor_locator(plticker.MaxNLocator(50))
    self.ax.get_yaxis().set_minor_locator(plticker.MaxNLocator(50))

    #format ticks and rotate the labels:
    self.ax.grid(b=True, which=&#39;major&#39;, linestyle=&#39;-&#39;, linewidth=&#39;1.0&#39;, color=&#39;gainsboro&#39;, zorder=0,
                 figure=self.fig)
    self.ax.grid(b=True, which=&#39;minor&#39;, linestyle=&#39;:&#39;, linewidth=&#39;0.5&#39;, color=&#39;silver&#39;, zorder=0, figure=self.fig)

    plt.xticks(rotation=70)</code></pre>
</details>
</dd>
<dt id="src.IO_files_creator.graphs.Graph.show_and_save"><code class="name flex">
<span>def <span class="ident">show_and_save</span></span>(<span>self, path_of_save_folder: str, name: str)</span>
</code></dt>
<dd>
<div class="desc"><p>shows and saves the figure - must be called to show the figure at the end of plotting
:param self:
:param path_of_save_folder: save figures to this folder
:param name: save figures under this name
:return:</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def show_and_save(self, path_of_save_folder: str, name: str):
    &#34;&#34;&#34;
    shows and saves the figure - must be called to show the figure at the end of plotting
    :param self:
    :param path_of_save_folder: save figures to this folder
    :param name: save figures under this name
    :return:
    &#34;&#34;&#34;
    plt.show()
    plt.savefig(path_of_save_folder + name)</code></pre>
</details>
</dd>
</dl>
</dd>
<dt id="src.IO_files_creator.graphs.Solution"><code class="flex name class">
<span>class <span class="ident">Solution</span></span>
<span>(</span><span>path_to_solution_folder)</span>
</code></dt>
<dd>
<div class="desc"><p>This takes a folder of .out files amnd converts them to a dictionary of pandas DataFrames.
Create 2 new dataframe columns for name1 and name2 as additional filtering criteria.
Write the names of failed runs to a file in the same folder called ERROR_RUNS.txt as these cannot be plotted.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class Solution():
    &#34;&#34;&#34;
    This takes a folder of .out files amnd converts them to a dictionary of pandas DataFrames.
    Create 2 new dataframe columns for name1 and name2 as additional filtering criteria.
    Write the names of failed runs to a file in the same folder called ERROR_RUNS.txt as these cannot be plotted.
    &#34;&#34;&#34;

    def __init__(self, path_to_solution_folder):
        self.sol = path_to_solution_folder

        # dictionary to store dataframes:
        self.df_dict = {}
        self.sol_to_df()

    def filter_txt(self, lines, add_X_col: bool = False):
        &#34;&#34;&#34;
        Use RegEx expression to find DataFrame col values and data and save them as two lists from .out file.
        :param lines: .out file formatted as &#39;/n&#39; seperated list of strings
        :param add_X_col: True adds an extra X(cm) column header.
        :return:
        &#34;&#34;&#34;
        col_list = []
        key_list = []
        col_tuple = [()]
        previous: str = &#34;&#34;
        row = []

        for line in enumerate(lines):
            if line[1].startswith(&#39;    1   &#39;):
                # get list of keys from row above the row starting with &#34;    1   &#34;
                new_key_list = re.findall(r&#34;\b[A-Z]{1}[\S]*&#34;, previous)
                if add_X_col == True:
                    new_key_list.insert(0, &#39;X(cm)&#39;)
                new_key_list.insert(0, &#34;Index&#34;)
                key_list = new_key_list

            # get list of columns from the row starting with &#34;    1   &#34; onwards until the next newline and format
            if not line[1].isspace():
                col_tuple = re.findall(r&#34;([-+]?[\d]+[\.]?[\d]*[E]?[-+]?[\d]+\b)|\s([\d]+)\s&#34;, line[1])
                if col_tuple != []:
                    row = [tup[0] or tup[1] for tup in col_tuple]
                    col_list.append(row)

            previous = line[1]

        return key_list, col_list

    def add_name_cols(self, out_file_name, df: pd.DataFrame):
        &#34;&#34;&#34;
        Add name1 and name2 columns to dataframe for filtering purposes. Use the actual name of the file to extract them.
        :param out_file_name: The name of solution .out file for processing
        :param df: The dataframe.
        :return:
        &#34;&#34;&#34;
        name = out_file_name.strip(&#34;.out&#34;)
        name1 = name.split(&#39;__&#39;)[0]
        name2 = name.split(&#39;__&#39;)[1]
        df[&#39;name1&#39;] = name1
        df[&#39;name2&#39;] = name2
        return df

    def sol_to_df(self):
        &#34;&#34;&#34;
        prints all failed files to a text file and transfers all other files to a DataFrame. Initialises an ERROR_RUNS.TXT file.
        Writes all file names with errors to these files instead of converting them to a DataFrame.
        :return:
        &#34;&#34;&#34;
        new_df = pd.DataFrame()

        # initalise an error file:
        txt_path = path.join(self.sol, &#34;ERROR_RUNS.txt&#34;)
        with open(txt_path, &#34;w&#34;) as error_file:
            error_file.write(&#34;The following files have errors and cannot be plotted: &#34;)

        # go through all .out files in solutions folder:
        for file in listdir(self.sol):
            if file.endswith(&#34;.out&#34;):
                full_path = path.join(self.sol, file)

                # readlines and if ERROR present in the file, write the name of file to error_file, otherwise create dataframe with data:
                with open(full_path, &#34;r&#34;) as f:
                    lines = f.readlines()
                    if any(&#34;ERROR&#34; in s for s in lines):
                        with open(txt_path, &#34;a&#34;) as error_file:
                            error_file.write(&#34;\n&#34; + file)
                    else:
                        whole_doc = &#39; &#39;.join(lines)
                        whole_doc = whole_doc.split(&#39; TWOPNT: &#39;, 1)[0]

                        # create new dataframe and a super new dataframe for every slice of data seperated by &#39;MOLE FRACTION&#39;
                        i = 0
                        filtered_lines = whole_doc.split(&#34;MOLE FRACTION&#34;)
                        for i in range(len(filtered_lines)):
                            split_filtered = filtered_lines[i].split(&#39;\n&#39;)

                            if i == 0:
                                key_list, col_list = self.filter_txt(split_filtered, add_X_col=False)
                                new_df = pd.DataFrame(col_list, columns=key_list)
                            else:
                                # merge all successive dataframes to inital dataframe on X(cm) as merge column:
                                key_list, col_list = self.filter_txt(split_filtered, add_X_col=True)
                                super_new_df = pd.DataFrame(col_list, columns=key_list)
                                super_new_df.drop(&#39;Index&#39;, axis=1, inplace=True)
                                new_df = new_df.merge(super_new_df, on=&#39;X(cm)&#39;)
                    name = file.strip(&#39;.out&#39;)
                    new_df = self.add_name_cols(file, new_df)
                    self.df_dict[name] = new_df</code></pre>
</details>
<h3>Methods</h3>
<dl>
<dt id="src.IO_files_creator.graphs.Solution.add_name_cols"><code class="name flex">
<span>def <span class="ident">add_name_cols</span></span>(<span>self, out_file_name, df: pandas.core.frame.DataFrame)</span>
</code></dt>
<dd>
<div class="desc"><p>Add name1 and name2 columns to dataframe for filtering purposes. Use the actual name of the file to extract them.
:param out_file_name: The name of solution .out file for processing
:param df: The dataframe.
:return:</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def add_name_cols(self, out_file_name, df: pd.DataFrame):
    &#34;&#34;&#34;
    Add name1 and name2 columns to dataframe for filtering purposes. Use the actual name of the file to extract them.
    :param out_file_name: The name of solution .out file for processing
    :param df: The dataframe.
    :return:
    &#34;&#34;&#34;
    name = out_file_name.strip(&#34;.out&#34;)
    name1 = name.split(&#39;__&#39;)[0]
    name2 = name.split(&#39;__&#39;)[1]
    df[&#39;name1&#39;] = name1
    df[&#39;name2&#39;] = name2
    return df</code></pre>
</details>
</dd>
<dt id="src.IO_files_creator.graphs.Solution.filter_txt"><code class="name flex">
<span>def <span class="ident">filter_txt</span></span>(<span>self, lines, add_X_col: bool = False)</span>
</code></dt>
<dd>
<div class="desc"><p>Use RegEx expression to find DataFrame col values and data and save them as two lists from .out file.
:param lines: .out file formatted as '/n' seperated list of strings
:param add_X_col: True adds an extra X(cm) column header.
:return:</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def filter_txt(self, lines, add_X_col: bool = False):
    &#34;&#34;&#34;
    Use RegEx expression to find DataFrame col values and data and save them as two lists from .out file.
    :param lines: .out file formatted as &#39;/n&#39; seperated list of strings
    :param add_X_col: True adds an extra X(cm) column header.
    :return:
    &#34;&#34;&#34;
    col_list = []
    key_list = []
    col_tuple = [()]
    previous: str = &#34;&#34;
    row = []

    for line in enumerate(lines):
        if line[1].startswith(&#39;    1   &#39;):
            # get list of keys from row above the row starting with &#34;    1   &#34;
            new_key_list = re.findall(r&#34;\b[A-Z]{1}[\S]*&#34;, previous)
            if add_X_col == True:
                new_key_list.insert(0, &#39;X(cm)&#39;)
            new_key_list.insert(0, &#34;Index&#34;)
            key_list = new_key_list

        # get list of columns from the row starting with &#34;    1   &#34; onwards until the next newline and format
        if not line[1].isspace():
            col_tuple = re.findall(r&#34;([-+]?[\d]+[\.]?[\d]*[E]?[-+]?[\d]+\b)|\s([\d]+)\s&#34;, line[1])
            if col_tuple != []:
                row = [tup[0] or tup[1] for tup in col_tuple]
                col_list.append(row)

        previous = line[1]

    return key_list, col_list</code></pre>
</details>
</dd>
<dt id="src.IO_files_creator.graphs.Solution.sol_to_df"><code class="name flex">
<span>def <span class="ident">sol_to_df</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><p>prints all failed files to a text file and transfers all other files to a DataFrame. Initialises an ERROR_RUNS.TXT file.
Writes all file names with errors to these files instead of converting them to a DataFrame.
:return:</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def sol_to_df(self):
    &#34;&#34;&#34;
    prints all failed files to a text file and transfers all other files to a DataFrame. Initialises an ERROR_RUNS.TXT file.
    Writes all file names with errors to these files instead of converting them to a DataFrame.
    :return:
    &#34;&#34;&#34;
    new_df = pd.DataFrame()

    # initalise an error file:
    txt_path = path.join(self.sol, &#34;ERROR_RUNS.txt&#34;)
    with open(txt_path, &#34;w&#34;) as error_file:
        error_file.write(&#34;The following files have errors and cannot be plotted: &#34;)

    # go through all .out files in solutions folder:
    for file in listdir(self.sol):
        if file.endswith(&#34;.out&#34;):
            full_path = path.join(self.sol, file)

            # readlines and if ERROR present in the file, write the name of file to error_file, otherwise create dataframe with data:
            with open(full_path, &#34;r&#34;) as f:
                lines = f.readlines()
                if any(&#34;ERROR&#34; in s for s in lines):
                    with open(txt_path, &#34;a&#34;) as error_file:
                        error_file.write(&#34;\n&#34; + file)
                else:
                    whole_doc = &#39; &#39;.join(lines)
                    whole_doc = whole_doc.split(&#39; TWOPNT: &#39;, 1)[0]

                    # create new dataframe and a super new dataframe for every slice of data seperated by &#39;MOLE FRACTION&#39;
                    i = 0
                    filtered_lines = whole_doc.split(&#34;MOLE FRACTION&#34;)
                    for i in range(len(filtered_lines)):
                        split_filtered = filtered_lines[i].split(&#39;\n&#39;)

                        if i == 0:
                            key_list, col_list = self.filter_txt(split_filtered, add_X_col=False)
                            new_df = pd.DataFrame(col_list, columns=key_list)
                        else:
                            # merge all successive dataframes to inital dataframe on X(cm) as merge column:
                            key_list, col_list = self.filter_txt(split_filtered, add_X_col=True)
                            super_new_df = pd.DataFrame(col_list, columns=key_list)
                            super_new_df.drop(&#39;Index&#39;, axis=1, inplace=True)
                            new_df = new_df.merge(super_new_df, on=&#39;X(cm)&#39;)
                name = file.strip(&#39;.out&#39;)
                new_df = self.add_name_cols(file, new_df)
                self.df_dict[name] = new_df</code></pre>
</details>
</dd>
</dl>
</dd>
</dl>
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
<li><code><a title="src.IO_files_creator" href="index.html">src.IO_files_creator</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="src.IO_files_creator.graphs.Graph" href="#src.IO_files_creator.graphs.Graph">Graph</a></code></h4>
<ul class="">
<li><code><a title="src.IO_files_creator.graphs.Graph.add_best_fit_line" href="#src.IO_files_creator.graphs.Graph.add_best_fit_line">add_best_fit_line</a></code></li>
<li><code><a title="src.IO_files_creator.graphs.Graph.add_error_bar" href="#src.IO_files_creator.graphs.Graph.add_error_bar">add_error_bar</a></code></li>
<li><code><a title="src.IO_files_creator.graphs.Graph.add_format" href="#src.IO_files_creator.graphs.Graph.add_format">add_format</a></code></li>
<li><code><a title="src.IO_files_creator.graphs.Graph.add_scatter_sol" href="#src.IO_files_creator.graphs.Graph.add_scatter_sol">add_scatter_sol</a></code></li>
<li><code><a title="src.IO_files_creator.graphs.Graph.add_scatter_spreadsheet" href="#src.IO_files_creator.graphs.Graph.add_scatter_spreadsheet">add_scatter_spreadsheet</a></code></li>
<li><code><a title="src.IO_files_creator.graphs.Graph.set_grid_ticks" href="#src.IO_files_creator.graphs.Graph.set_grid_ticks">set_grid_ticks</a></code></li>
<li><code><a title="src.IO_files_creator.graphs.Graph.show_and_save" href="#src.IO_files_creator.graphs.Graph.show_and_save">show_and_save</a></code></li>
</ul>
</li>
<li>
<h4><code><a title="src.IO_files_creator.graphs.Solution" href="#src.IO_files_creator.graphs.Solution">Solution</a></code></h4>
<ul class="">
<li><code><a title="src.IO_files_creator.graphs.Solution.add_name_cols" href="#src.IO_files_creator.graphs.Solution.add_name_cols">add_name_cols</a></code></li>
<li><code><a title="src.IO_files_creator.graphs.Solution.filter_txt" href="#src.IO_files_creator.graphs.Solution.filter_txt">filter_txt</a></code></li>
<li><code><a title="src.IO_files_creator.graphs.Solution.sol_to_df" href="#src.IO_files_creator.graphs.Solution.sol_to_df">sol_to_df</a></code></li>
</ul>
</li>
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