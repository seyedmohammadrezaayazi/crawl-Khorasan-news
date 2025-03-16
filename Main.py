import Scaping
import baseUrl

if __name__ == '__main__':
    urls = []
    up = 20966
    down = 20965
    namefile_excel= "kordad_1401_dorooz"

    urls.append(
        baseUrl.URL("http://khorasannews.com/", "خراسان", [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], up,
                    down))
    urls.append(
        baseUrl.URL("http://khorasanrazavi.khorasannews.com/", "خراسان رضوی", [2, 3, 4, 6, 7, 8, 9, 10, 11, 12], up,
                    down))
    urls.append(
        baseUrl.URL("http://khorasanshomali.khorasannews.com/", "خراسان شمالی", [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    up, down))
    urls.append(
        baseUrl.URL("http://khorasanjonobi.khorasannews.com/", "خراسان جنوبی", [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], up,
                    down))
    urls.append(
        baseUrl.URL("http://zendegisalam.khorasannews.com/", "زندگی سلام", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], up,
                    down))
    # urls.append(
    #     baseUrl.URL("http://zendegisalam.khorasannews.com/", "زندگی سلام", [1], up,
    #                 down))

    scape = Scaping.Scape(urls, namefile_excel)
    scape.run()
    scape.final()
