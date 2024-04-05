new Vue({
    delimiters: ['[[', ']]'],
    el:'#appSuple4m',
    data:{
        lists: [],
        errors: [],
        total: 0,
        cumple: 0,
        nocumple: 0,
        avan: 0,
        year: 0,
        month: 0,
    },
    created:function(){
        this.listYears();
    },
    methods:{
        listYears: function(){
            let fec = new Date();
            var selectYear = document.getElementById("year");
            for(var i = 2023; i<=fec.getFullYear(); i++)selectYear.options.add(new Option(i,i));
            var selectMonth = document.getElementById("month");
            for(var i = 1; i<=12; i++)selectMonth.options.add(new Option((new Intl.DateTimeFormat('es-ES', { month: 'long'}).format(fec.setMonth(i - 1))).toUpperCase(),i));
        },

        searchTeen: function(){
            var self = this
            let miFecha = new Date();
            if(this.year == 0 && this.month==0){
                var nameMonth = new Intl.DateTimeFormat('es-ES', { month: 'long'}).format(miFecha.setMonth(miFecha.getMonth()));
                this.year = miFecha.getFullYear();
                this.month = miFecha.getMonth() + 1;
            }
            else{
                var nameMonth = new Intl.DateTimeFormat('es-ES', { month: 'long'}).format(miFecha.setMonth(this.month - 1));
            }
            $('.nameMonthYear').text(nameMonth.toUpperCase()+' '+this.year);
            $(".nominalTable").removeAttr("id");
            $(".nominalTable").attr("id","tableNominal");

            axios.get('list/', { params: { year: this.year, month: this.month } })
            .then(function (response) {
                self.lists = response.data
                self.total = response.data[2].total
                self.cumple = response.data[2].cumple
                self.nocumple = response.data[2].total - response.data[2].cumple
                self.avan = response.data[2].avance
                setTimeout(function() {
                    $('table').trigger('footable_redraw');
                    $('.chart').data('easyPieChart').update(self.avan);
                    // $('.chart').data('easyPieChart').options.barColor = '#0033CC';
                }, 100);
            });
        },

        PrintExcel() {
            url_ = window.location.origin + window.location.pathname + 'printExcel/?year='+this.year+'&month='+this.month;
            window.open(url_, '_parent');
        },

        listNoCumplen: function(){
            $(".nominalTable").removeAttr("id");
            $(".nominalTable").attr("id","tableNominalNoCumple");
            this.listNoSuplement = [];
            for (let i = 0; i < this.lists[0].length; i++) {
                if(this.lists[0][i].fields.num == 0){
                    this.listNoSuplement.push(this.lists[0][i]);
                }
            }
            let milistView = []
            milistView.push(this.listNoSuplement, this.lists[1], this.lists[2]);
            this.lists = milistView;

            setTimeout(function() {
                $('table').trigger('footable_redraw');
            }, 100);
        }
    },
})