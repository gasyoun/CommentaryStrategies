// script.js
// Функция, которая будет вызываться при появлении элементов в области видимости
function handleIntersection(entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            var element = entry.target;
            highlightLatinText(element);
            observer.unobserve(element); // Остановка отслеживания этого элемента, после того как он станет видимым
        }
    });
}

// Создаем новый Intersection Observer
const observer = new IntersectionObserver(handleIntersection, { threshold: 0.5 });

document.addEventListener('DOMContentLoaded', function() {
    const start = performance.now();
    var classNames = ['translation', 'translation2', 'comment_text'];

    classNames.forEach(function(className) {
        var elementsWithClass = document.querySelectorAll('.' + className);

        elementsWithClass.forEach(function(element) {
            highlightLatinText(element);
        });
    });
    const end = performance.now();
    const executionTime = end - start;
    console.log('Время выполнения: ' + executionTime + ' мс');
});

function highlightLatinText(element) {
    // Создаем временный элемент div
    var tempDiv = document.createElement('div');
    tempDiv.innerHTML = element.innerHTML;

    // Обрабатываем латинские буквы внутри текстовых узлов
    processTextNodes(tempDiv);
    processDigitalNodes(tempDiv);
    // Заменяем содержимое элемента обработанным HTML
    element.innerHTML = tempDiv.innerHTML;
}

// Unicode-aware: подсветка последовательностей латинских букв (включая диакритику/combining marks)
function processTextNodes(parentNode) {
    // (^|[^\p{L}])  — начало строки или символ, не являющийся буквой
    // ((?:\p{Script=Latin}|\p{M})+) — одна или более латинских букв или combining marks
    // (?=$|[^\p{L}]) — перед концом строки или не-буквой
    const latinRegex = /(^|[^\p{L}])((?:\p{Script=Latin}|\p{M})+)(?=$|[^\p{L}])/gu;

    for (let i = 0; i < parentNode.childNodes.length; i++) {
        const node = parentNode.childNodes[i];

        if (node.nodeType === 3) { // текстовый узел
            const original = node.nodeValue;
            const newText = original.replace(latinRegex, (m, p1, p2) => {
                return p1 + '<span class="blue-text">' + p2 + '</span>';
            });

            if (newText !== original) {
                const tempSpan = document.createElement('span');
                tempSpan.innerHTML = newText;
                parentNode.replaceChild(tempSpan, node);
            }
        } else if (node.nodeType === 1) { // элемент
            const tag = node.tagName && node.tagName.toUpperCase();
            if (tag !== 'SCRIPT' && tag !== 'STYLE') {
                processTextNodes(node);
            }
        }
    }
}

function processDigitalNodes(parentNode) {
    // Подсвечиваем любые десятичные цифры Unicode (\p{Nd})
    const digitRegex = /(^|[^\p{Nd}])(\p{Nd}+)(?=$|[^\p{Nd}])/gu;

    for (let i = 0; i < parentNode.childNodes.length; i++) {
        const node = parentNode.childNodes[i];

        if (node.nodeType === 3) {
            const original = node.nodeValue;
            const newText = original.replace(digitRegex, (m, p1, p2) => {
                return p1 + '<span class="red-text">' + p2 + '</span>';
            });

            if (newText !== original) {
                const tempSpan = document.createElement('span');
                tempSpan.innerHTML = newText;
                parentNode.replaceChild(tempSpan, node);
            }
        } else if (node.nodeType === 1) {
            const tag = node.tagName && node.tagName.toUpperCase();
            if (tag !== 'SCRIPT' && tag !== 'STYLE') {
                processDigitalNodes(node);
            }
        }
    }
}
