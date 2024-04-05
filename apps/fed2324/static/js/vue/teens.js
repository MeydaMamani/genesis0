new Vue({
    delimiters: ['[[', ']]'],
    el:'#appTeens',
    data:{
        lists: [],
        listMicroRed: [],
        listDistricts: [],
        errors: [],
        total: 0,
        cumple: 0,
        nocumple: 0,
        avan: 0,
        year: 0,
        month: 0,
        red: 'TODOS',
        microred: 'TODOS',
        distrito: 'TODOS',
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
            for(var i = 1; i<=12; i++)selectMonth.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));
        },

        listMcrRed(e) {
            var id = e.target.value.split(/\s*-\s*/);
            axios.get('filterMicroRed/', { params: { id: id[0] } })
            .then(respuesta => {
                this.listMicroRed = respuesta.data
            });
        },

        listDistritos(e) {
            var id = e.target.value.split(/\s*-\s*/);
            axios.get('filterDist/', { params: { id: id[0] } })
            .then(respuesta => {
                this.listDistricts = respuesta.data
            });
        },

        searchTeen: function(e){
            var self = this
            var csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
            var formData = new FormData(e.target)

            if(this.year == 0 && this.month==0){
                var nameMonth = new Date().toLocaleString('default', { month: 'long' });
                this.year = new Date().getFullYear();
                this.month = new Date().getMonth() + 1;
                let red_user = $("#red").val();
                let mcred_user = $("#microred").val();
                (red_user != "TODOS") ? formData.set('red', red_user) : formData.set('red', 'TODOS');
                (mcred_user != "TODOS") ? formData.set('microred', mcred_user) : formData.set('microred', 'TODOS');
                formData.set('year', this.year);
                formData.set('month', this.month);
            }
            else{
                var nameMonth = new Date(this.month.toString()).toLocaleString('default', { month: 'long' });
            }
            $('.nameMonthYear').text(nameMonth.toUpperCase()+' '+this.year);
            $(".nominalTable").removeAttr("id");
            $(".nominalTable").attr("id","tableNominal");

            axios({
                headers: { 'X-CSRFToken': csrfmiddlewaretoken, 'Content-Type': 'multipart/form-data' },
                method: 'POST',
                url: 'list/',
                data: formData
            }).then(response => {
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
            }).catch(e => {
                this.errors.push(e)
            })
        },

        PrintExcel() {
            let red = $("#red").val();
            let mcrred = $("#microred").val();
            let dist = $("#distrito").val();
            url_ = window.location.origin + window.location.pathname + 'printExcel/?red='+red+'&microred='+mcrred+'&dist='+dist+'&year='+this.year +'&month='+this.month;
            window.open(url_, '_parent');
        },

        // listNoCumplen: function(){
        //     $(".nominalTable").removeAttr("id");
        //     $(".nominalTable").attr("id","tableNominalNoCumple");
        //     this.listNoSuplement = [];
        //     for (let i = 0; i < this.lists[0].length; i++) {
        //         if(this.lists[0][i].fields.num == 0){
        //             this.listNoSuplement.push(this.lists[0][i]);
        //         }
        //     }
        //     let milistView = []
        //     milistView.push(this.listNoSuplement, this.lists[1], this.lists[2]);
        //     this.lists = milistView;

        //     setTimeout(function() {
        //         $('table').trigger('footable_redraw');
        //     }, 100);
        // }
    },
})