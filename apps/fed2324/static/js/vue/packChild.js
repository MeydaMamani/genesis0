new Vue({
    delimiters: ['[[', ']]'],
    el:'#appPackChild',
    data:{
        lists: [],
        errors: [],
        month: 7,
        year: 2023,
        type: 'advance',
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

        PrintExcel() {
            let type=$( "#type" ).val(),
                year=$("#year").val(),
                month=$("#month").val();
            url_ = window.location.origin + window.location.pathname + 'printExcel/?year='+year+'&month='+month;
            window.open(url_, '_parent');
            console.log(year, month);
        },
    },
})