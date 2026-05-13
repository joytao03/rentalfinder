chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: "sendToRentalFinder",
        title: "Send to Rental Finder",
        contexts: ["selection"]
    });
});


chrome.contextMenus.onClicked.addListener((info, tab) => {

    const selectedText = info.selectionText;

    fetch("http://127.0.0.1:8000/extract", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: selectedText,
            url: tab.url,
            title: tab.title
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Rental data:", data);
        alert("Rental info extracted successfully!");
    })
    .catch(error => {
        console.error("Error:", error);
    });

});