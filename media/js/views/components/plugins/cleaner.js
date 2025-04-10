define([
    'knockout',
    'arches',
    'js-cookie',
    'templates/views/components/plugins/cleaner.htm'
], function(ko, arches, Cookies, CleanerDashboardTemplate) {

    const CleanerDashboardViewModel = function() {
        const self = this;
        this.loading = ko.observable(true);
        this.tests = ko.observable();
        this.graphs = ko.observableArray();
        this.selection = ko.observable();

        this.getStatus = async function() {
            const response = await window.fetch("/cleaner");
            const data = await response.json();
            self.tests(data.tests);
            self.graphs(data.graphs);
            self.selection(false);
            self.loading(false);
        };

        this.saveStatus = async function() {
            const response = await fetch("/cleaner", {
                method: 'POST',
                credentials: 'include',
                headers: {
                    "X-CSRFToken": Cookies.get('csrftoken')
                }
            });
            const data = await response.json();
        };

        this.getStatus();
    };

    return ko.components.register('cleaner', {
        viewModel: CleanerDashboardViewModel,
        template: CleanerDashboardTemplate
    });
});
