/*
http://css-tricks.com/examples/SimplejQueryDropdowns/
http://novice2ninja.ru/ninja-book/chapter-5/simple-accordion.html !!
*/
(function () {
    window.addEvent('domready', function() {
        /*
            Определить открытую сраницу
            выставить свойство открытая страница.
            Ей может быть
            <li><h1>Расписание</h1>
            </li>
            или
            <li><h1>Тренеры</h1>
                <ul>
                    <li>Алина</li>
                </ul>
            </li>
        */
        document.getElements('nav ul li ul li').each(function (link) {
            if (link.getElement('a') != null) //not current page.
                return;
            link.addClass('current-page');
            link.getParent().getParent().getElement('h1').addClass('current-page');

            link.getParent().getParent().addClass('opened');
        });
        document.getElements('nav > ul > li').each(function (li) {
            if (li.getElement('ul') == null && li.getElement('a') == null) {
                li.getElement('h1').addClass('current-page');
            }
        });

        var spaces = new Array();
        document.getElements('nav > ul > li > ul').each(function (ul) {
            var li = ul.getParent();
            li.addEvent("click", function () {
                if (this.hasClass('opened'))
                    return;
                spaces.each(function (li) {
                    li.removeClass('opened');
                });
                this.addClass('opened');
            });

            spaces.push(li);
        });

    });
})();

