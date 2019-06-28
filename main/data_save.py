# -*- coding: utf-8 -*-
import time

STYLE = r"""<style type="text/css">
table.hovertable {
	font-family: verdana,arial,sans-serif;
	font-size:11px;
	color:#333333;
	border-width: 1px;
	border-color: #999999;
	border-collapse: collapse;
}
table.hovertable th {
	background-color:#c3dde0;
	border-width: 1px;
	padding: 8px;
	border-style: solid;
	border-color: #a9c6c9;
}
table.hovertable tr {
	background-color:#d4e3e5;
}
table.hovertable td {
	border-width: 1px;
	padding: 8px;
	border-style: solid;
	border-color: #a9c6c9;
}
</style>"""


class DataSave(object):
    def save_data(self, datas, sort_by):
        file_name = 'give_rating_%s_%s.html' % (sort_by, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        file_out = open(file_name, 'w')
        file_out.write(r'''<meta http-equiv=Content-Type content="text/html;charset=utf-8">
        <html>
        %s
        <body>
        ''' % STYLE)
        no = 1
        totalScore = 0.0
        data_rating1 = ""
        data_rating2 = ""
        data_rating3 = ""
        data_rating4 = ""
        data_rating5 = ""
        for data in datas:
            score = int(data['im:rating']['label'])
            if score == 1:
                data_rating1 += self.get_tr_content(data, no)
            elif score == 5:
                data_rating5 += self.get_tr_content(data, no)
            elif score == 2:
                data_rating2 += self.get_tr_content(data, no)
            elif score == 3:
                data_rating3 += self.get_tr_content(data, no)
            else:
                data_rating4 += self.get_tr_content(data, no)
            totalScore += score
            no += 1

        file_out.write(r'''<h1>Avg Score: %.1f Sort by %s</h1>''' % ((totalScore / no), sort_by))
        if len(data_rating1) != 0:
            file_out.write(self.get_table_content('Bad review', data_rating1))
        if len(data_rating2) != 0:
            file_out.write(self.get_table_content('Two stars', data_rating2))
        if len(data_rating3) != 0:
            file_out.write(self.get_table_content('Three Star', data_rating3))
        if len(data_rating4) != 0:
            file_out.write(self.get_table_content('Four stars', data_rating4))
        if len(data_rating5) != 0:
            file_out.write(self.get_table_content('Praise', data_rating5))

        file_out.write(r"""</body>
        </html>""")
        file_out.close()

        return file_name

    def get_table_content(self, rating, data_rating):
        return unicode(r"""<h4>%s</h4>
            <table  class='hovertable'>
            <tr><th>NO</th><th>AUTHOR</th><th>TITLE</th><th>CONTENT</th><th>VERSION</th><th>RATING</th></tr>
            %s
            </table><br>""" % (rating, data_rating)).encode('utf-8')

    def get_tr_content(self, data, no):
        return r"""<tr  onmouseover="this.style.backgroundColor='#ffff66';" onmouseout="this.style.backgroundColor='#d4e3e5';">
                <td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>
                </tr>""" % (
            no, data['author']['name']['label'], data['title']['label'], data['content']['label'],
            data['im:version']['label'], data['im:rating']['label'])
