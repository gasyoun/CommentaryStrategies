document.addEventListener("keydown", function(e) {
  if (e.key === "F1" && (e.ctrlKey || e.metaKey)) {
    e.preventDefault();
    const selection = window.getSelection();
    const sel = selection.toString().trim();

    if (sel) {
      // Определяем элемент, в котором находится выделение
      let node = selection.anchorNode;
      if (node && node.nodeType === Node.TEXT_NODE) {
        node = node.parentElement;
      }

      // Собираем цепочку классов вверх по дереву и фиксируем последний ID
      let classesPath = [];
      let current = node;
      let lastId = null;

      while (current && current.nodeType === Node.ELEMENT_NODE) {
        if (current.className) {
          let info = current.className.toString().trim();
          if (current.id) {
            info += " (id: " + current.id + ")";
            if (!lastId) {
              lastId = current.id; // первый (самый глубокий) id
            }
          }
          classesPath.unshift(info);
        }
        current = current.parentElement;
      }

      const classesInfo = classesPath.length 
        ? "Цепочка классов:\n" + classesPath.join(" > ") 
        : "Классы не найдены.";

      const linkInfo = lastId 
        ? "Ссылка для перехода: " + window.location.href.split('#')[0] + "#" + lastId
        : "Ссылка для перехода: [нет ID]";

      // Формируем письмо
      const subject = encodeURIComponent("Сообщение об ошибке -"+ document.title);
      const body = encodeURIComponent(
        "Обнаружен фрагмент с ошибкой:\n\n" + sel +
        "\n\n" + "Правильное написание фрагмента:" +
        "\n\n" + "[на что исправить]" +
        "\n\n" + classesInfo +
        "\n\n" + linkInfo
      );

      // Открываем письмо в новой вкладке
      window.open(
        `mailto:corpus.error@gmail.com?subject=${subject}&body=${body}`,
        "_blank"
      );
    }
  }
});
