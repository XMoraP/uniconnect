var fundTableTemplateSource = document.getElementById('fundTableTemplate').innerHTML;
var fundTableTemplate = Handlebars.compile(fundTableTemplateSource);
document.getElementById('handlebarsFundTable').innerHTML = fundTableTemplate(fundData);