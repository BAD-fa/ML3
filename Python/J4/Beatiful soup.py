import re


class HTMLParser:
    def __init__(self, html_doc):
        self.html_doc: str = html_doc
        pass

    def set_html_doc(self, html_doc):
        self.html_doc = html_doc

    def find_first(self, output_arg, **finding_args):
        pass

    def find_all(self, n, output_arg, **finding_args):
        pass

    def find_parent(self, output_arg, **finding_args):
        pass

    def find_grandparent(self, n, output_arg, **finding_args):
        pass

    def remove_comment(self, **finding_args):
        pass

    def remove_all_comments(self):
        pass

    def remove_tag(self, **finding_args):
        pass

    def custom_find(self, **finding_args):
        temp = self.html_doc
        result = []
        if finding_args.get("name"):
            result = re.findall("<" + finding_args.get("name") + "(.*?)>(.*?)<\/" + finding_args.get("name") + ">",
                                self.html_doc)
        if finding_args.get("id"):
            if result:
                for elm in result.copy():
                    if f"id='{finding_args.get('id')}'" not in elm[0]:
                        result.remove(elm)
            # else:
            #     result = re.findall("(<(.*?)id=\"|'" + finding_args.get("id") + "\"|'.*?>)(.*?)(<\/(.*?)>)",
            #                         self.html_doc)
        if finding_args.get("class"):
            pass
        if finding_args.get("string"):
            pass

        return result


if __name__ == '__main__':
    parser = HTMLParser("<b>some text.</b><b id='1'>some text.</b><b id='2' class='abcd'>some text.</b><b>some "
                        "text.</b>")

    print(parser.custom_find(name="b", id="2"))
