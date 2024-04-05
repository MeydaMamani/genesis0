new Vue({
    delimiters: ['[[', ']]'],
    el:'#appCoverage',
    data:{
        errors: [],
        listLess1year_cant: [],
    },
    created:function(){
        this.listYears();
    },
    methods:{
        listYears: function(){
            var selectMonth = document.getElementById("mes");
            for(var i = 1; i<=12; i++)selectMonth.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));
        },

        formRn: function(){
            id=2
            axios.get('listrn/', { params: { id: id } })
            .then(respuesta => {
                this.listLess1year_cant = respuesta.data[0]
                console.log(this.listLess1year_cant);
                setTimeout(function() {
                    $('#chartBcg').data('easyPieChart').update(respuesta.data[0].av_bcg);
                    $('#chartHvb').data('easyPieChart').update(respuesta.data[0].av_hvb);
                    $('#chartApo').data('easyPieChart').update(respuesta.data[0].av_apo);
                    $('#chartPenta').data('easyPieChart').update(respuesta.data[0].av_penta);
                    $('#chartRota').data('easyPieChart').update(respuesta.data[0].av_rota);
                    $('#chartNeumo').data('easyPieChart').update(respuesta.data[0].av_neumo);
                    $('#chartBcg').data('easyPieChart').options.barColor = '#1E88E5';
                    $('#chartHvb').data('easyPieChart').options.barColor = '#1E88E5';
                    // $('#chartApo').data('easyPieChart').options.barColor = '#694ba8';
                }, 100);
            });
        },
    }
})