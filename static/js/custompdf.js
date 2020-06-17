console.log("test")
pdfjsLib.getDocument('/static/img/resume/CJ_Storrs_Resume.pdf').then(function (pdf) {
    console.log("pdf loaded");
    pdf.getPage(1).then(function (page) {
        var scale = 1.5;
        var viewport = page.getViewport(scale);

        var canvas = document.getElementById('the-canvas');
        var context = canvas.getContext('2d');
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        var renderContext = {
            canvasContext: context,
            viewport: viewport
        };
        page.render(renderContext);
    });
});