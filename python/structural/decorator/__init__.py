"""
 Преимущества и недостатки
 Большая гибкость, чем у наследования.
 Позволяет добавлять обязанности на лету.
 Можно добавлять несколько новых обязанностей сразу.
 Позволяет иметь несколько мелких объектов вместо одного объекта на все случаи жизни.

Трудно конфигурировать многократно обёрнутые объекты.
 Обилие крошечных классов.

Отношения с другими паттернами
Адаптер меняет интерфейс существующего объекта. Декоратор улучшает другой объект без изменения его интерфейса. Причём Декоратор поддерживает рекурсивную вложенность, чего не скажешь об Адаптере.

Адаптер предоставляет классу альтернативный интерфейс. Декоратор предоставляет расширенный интерфейс. Заместитель предоставляет тот же интерфейс.

Цепочка обязанностей и Декоратор имеют очень похожие структуры. Оба паттерна базируются на принципе рекурсивного выполнения операции через серию связанных объектов. Но есть и несколько важных отличий.

Обработчики в Цепочке обязанностей могут выполнять произвольные действия, независимые друг от друга, а также в любой момент прерывать дальнейшую передачу по цепочке. С другой стороны Декораторы расширяют какое-то определённое действие, не ломая интерфейс базовой операции и не прерывая выполнение остальных декораторов.
"""