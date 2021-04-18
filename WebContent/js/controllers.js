var portfolioApp = angular.module('portfolioApp',[]);

portfolioApp.controller('GalleryListCtrl', function($scope) {
    $scope.galleries = [
        {
            'title':'Zdjęcie gór #1','section':'Góry' , 'when':'2019-07-10', 'thumbnailUrl':'img/gory/1.jpg'
        },{
            'title':'Zdjęcie gór #2','section':'Góry' , 'when':'2015-07-12', 'thumbnailUrl':'img/gory/4.jpg'
        },{
            'title':'Zdjęcie jeziora #1','section':'Jeziora' , 'when':'2016-08-02', 'thumbnailUrl':'img/jeziora/2.jpg'
        },{
            'title':'Zdjęcie jeziora #2','section':'Jeziora' , 'when':'2018-03-12', 'thumbnailUrl':'img/jeziora/5.jpg'
        },{
            'title':'Zdjęcie jeziora #3','section':'Jeziora' , 'when':'2017-05-26', 'thumbnailUrl':'img/jeziora/alt.jpg'
        },{
            'title':'Zdjęcie lasu #1','section':'Lasy' , 'when':'2014-11-18', 'thumbnailUrl':'img/lasy/3.jpg'
        }
    ];
});

