document.addEventListener("DOMContentLoaded", function () {
    const bodyElement = document.getElementById("bodyElement");
    const toggleThemeButtons = document.querySelectorAll("button[data-bs-theme-value]");

    // Recuperar el tema y el botón activo almacenados en LocalStorage
    let savedData = JSON.parse(localStorage.getItem("themeData"));

    if (!savedData) {
      savedData = {
        theme: "auto",
        btn: "auto"
      };
    }

    // Función para activar el botón correspondiente al tema activo
    function activateButtonForTheme(theme) {
      toggleThemeButtons.forEach(btn => {
        if (btn.getAttribute("data-bs-theme-value") === theme) {
          btn.classList.add("active");
        } else {
          btn.classList.remove("active");
        }
      });
    }

    bodyElement.setAttribute("data-bs-theme", savedData.theme);
    activateButtonForTheme(savedData.btn);

    toggleThemeButtons.forEach(button => {
      button.addEventListener("click", function () {
        const themeValue = button.getAttribute("data-bs-theme-value");

        // Actualizar el objeto de datos guardados
        savedData.theme = themeValue;
        savedData.btn = themeValue;

        // Guardar los datos actualizados en LocalStorage
        localStorage.setItem("themeData", JSON.stringify(savedData));

        if (themeValue === "auto") {
          if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
            bodyElement.setAttribute("data-bs-theme", "dark");
            // Actualizar el objeto de datos guardados
            savedData.theme = "dark";
            savedData.btn = themeValue;

            // Guardar los datos actualizados en LocalStorage
            localStorage.setItem("themeData", JSON.stringify(savedData));
          } else {
            bodyElement.setAttribute("data-bs-theme", "light");
            // Actualizar el objeto de datos guardados
            savedData.theme = "light";
            savedData.btn = themeValue;
            
            // Guardar los datos actualizados en LocalStorage
            localStorage.setItem("themeData", JSON.stringify(savedData));
          }
        } else if (themeValue === "dark") {
          bodyElement.setAttribute("data-bs-theme", "dark");
        } else if (themeValue === "light") {
          bodyElement.setAttribute("data-bs-theme", "light");
        }

        // Activar el botón correspondiente al tema seleccionado
        activateButtonForTheme(themeValue);
      });
    });
  });