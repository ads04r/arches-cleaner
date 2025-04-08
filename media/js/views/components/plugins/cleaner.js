define([
    'knockout',
    'arches',
    'js-cookie',
    'templates/views/components/plugins/cleaner.htm'
], function(ko, arches, Cookies, CleanerDashboardTemplate) {

    const CleanerDashboardViewModel = function() {
        const self = this;
        this.loading = ko.observable(true);
        this.records = ko.observable();

        this.getStatus = async function() {
            const response = await window.fetch("cleaner");
            const data = await response.json();
            self.resourceCount = data.resource_count;
            self.tileCount = data.tile_count;
            self.records(data.records);
            self.loading(false);
        };

        this.saveStatus = async function() {
            const response = await fetch("cleaner", {
                method: 'POST',
                credentials: 'include',
                headers: {
                    "X-CSRFToken": Cookies.get('csrftoken')
                }
            });
            const data = await response.json();
            self.records(data.records);
        };

        this.getStatus();
    };

    return ko.components.register('cleaner', {
        viewModel: CleanerDashboardViewModel,
        template: CleanerDashboardTemplate
    });
});
