class Html:
    def __init__(self):
        self.url = "Please_put_server_html_path"
        self.week = ['月','火','水','木','金','土']
        self.quarters = ['Q1', 'Q2', 'Q3', 'Q4']
        self.grade = ['3', '4', 'M1', 'M2', 'その他']
    
    
    def get_form(self, param = []):
        import cgi
        d = {}
        form = cgi.FieldStorage()
        for i in param:
            d[i] = form.getvalue(i)
            if i == "name":
                d[i] = self._check_script(d[i])
        return d

    
    def _check_script(self,data):
            if isinstance(data, str):
                return data.replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#39;")
            else:
                return data


    def char_encode(self):
        import io, sys
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            
            
    def print_header(self, title = "時間割管理"):
        print("Content-Type:text/html\n")
        print("<html lang=\"ja\">")
        print(f"<head><link rel=\"stylesheet\" href=\"sch.css\"><title>{title}</title></head>")
        print("<body>")


    def print_tail(self):
        print("</body></html>")


    def print_menu(self):
        print("""<header>
        <ul class = \"tag\">
        <li><a>時間割管理Web</a></li>
        <li><a class='menu' href = \"./home.py\">Home</a></li>
        <li><a class='menu' href = \"./user.py\">ユーザ一覧</a></li>
        </ul>
        </header>""")


    def make_tbody(self, arg):
        return '<tbody>' + arg + '</tbody>'


    def make_thead(self, result: list, null_space = False):
        table = "<thead><tr>"
        if null_space:
            table += '<th scope=\"col\"></th>'
        for i in result:
            table += f'<th scope=\"col\">{i}</th>'
        table += '</tr></thead>'
        return table


    def make_checkbox(self, grade: str, checked = False):
        if checked:
            return f'<input type=\"checkbox\" name=\"select\" value=\"{grade}\" checked=\"checked\">{grade}'
        else:
            return f'<input type=\"checkbox\" name=\"select\" value=\"{grade}\">{grade}'


    def form_tag_head(self, action = ""):
        return f"<form method=\"post\" action=\"{action}\">"
    
    
    def form_tag_tail(self, value):
        return f"<input type=\"submit\" value=\"{value}\"></form>"


    def make_input(self, input_type, name: str, value = "", option = ""):
        if value:
            return f'<input type=\"{input_type}\" name=\"{name}\" value=\"{value}\" {option}>'
        else:    
            return f'<input type=\"{input_type}\" name=\"{name}\" {option}>'


    def make_selector(self, name, options: list):
        selector = f'<select name=\"{name}\">'
        for option in options:
            selector += self.make_option_tag(option)
        selector += '</select>'
        return selector
    
    
    def make_option_tag(self, value: str):
        return f'<option value=\"{value}\">{value}</option>'


    def make_button(self, name: str, value: str, label: str):
        return f'<button type=\"submit\" name=\"{name}\" value=\"{value}\">{label}</button></form>'


    def make_radio(self, name: str, value, label, checked = False):
        if checked:
            return f'<div><label><input type=\"radio\" name=\"{name}\" value=\"{value}\" checked=\"checked\">{label}</label></div>'
        else:
            return f'<div><label><input type=\"radio\" name=\"{name}\" value=\"{value}\">{label}</label></div>'
        
        
    def make_table_head(self, caption: str):
        return f'<table><caption>{caption}</caption>' 


    def make_table_tail(self):
        return '</table>'