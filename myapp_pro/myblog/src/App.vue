<template>
  <div class="container">
    <div class="page-header">
      <my-name></my-name>
    </div>
    <div class="row">
      <div class="col-sm-3 col-sm-push-9 rightbar">
        <my-image></my-image>
        <h3>Contact Info</h3>
        <div class="rightblock">
          <ul>
            <li  v-for="item in MyItems" :key="item.id">
              <my-contact-info
                :label="item.label"
                :info="item.info"
                :id="item.id"
              ></my-contact-info>
            </li>
          </ul>
        </div>
      </div>

      <div class="col-sm-9 col-sm-pull-3 leftbar" style="font-family: 'JetBrainsMono-Regular'" >
        <!-- <p>I am an Associate Professor of Databaseology in the Computer Science Department at Carnegie Mellon University. My research interest is in database management systems, specifically main memory systems, self-driving / autonomous architectures, transaction processing systems, and large-scale data analytics. At CMU, I am a member of the  -->
        <!-- </p> -->
        <p>I am currently an undergraduate student at China University of Geosciences in Beijing, and I am interested in network security and binary related issues. In the future, I will have the opportunity to further study computer-related knowledge, although I major in materials chemistry.</p>
          <h2>Education:</h2>
            <ul>
              <li  v-for="item in eduItems" :key="item.id">
                <my-exper
                :name="item.name"
                :major="item.major"
                :date="item.date"
                :degree="item.degree"
                ></my-exper>
              </li>
            </ul>
          <h2>Award:</h2>
            <ul>
              <li v-for="item in awardItems" :key="item.id">
                <my-award
                :name="item.name"
                :date="item.date"
                ></my-award>
              </li>
            </ul>
          <h2>Project / publication:</h2>
            <ul>
              <li v-for="item in pubItems" :key="item.id">
                <my-pub
                :name="item.name"
                :date="item.date"
                :DOI="item.DOI"
                :title="item.title"
                :url="item.index"></my-pub>
              </li>
            </ul>
        </div>  
  </div>
</div>

</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import uniqueId from "lodash.uniqueid";
import MyContactInfo from "./components/MyContactInfo.vue"
import MyImage from "./components/MyImage.vue"
import MyName from "./components/MyName.vue"
import MyExper from "./components/MyExper.vue"
import { onMounted } from "vue";
import MyAward from "./components/MyAward.vue";
import MyPub from "./components/MyPub.vue";

export default {
  name: "app",
  inject:['reload'],
  components: {
    MyContactInfo,MyImage,MyName,MyExper,MyAward,MyPub,
  },

  setup(){
      onMounted (()=>{
        console.log('hello onmounted');
      })
    },
  data() {
          return {
            MyItems:[
              {id: uniqueId("to-do-"), label: "Phone:", info:"15501279578"},
              {id: uniqueId("to-do-"), label: "Email:", info:"lfh3485188464@163.com"},
              {id: uniqueId("to-do-"), label: "Undergraduate institution:", info:"  China University of Geosciences Beijing"},
              {id: uniqueId("to-do-"), label: "Github:", info:"https://github.com/Little-slash"},
          ],
          eduItems:[{
            // name:'',    // 学校名称
            // major:'',
            // degree:'',
            // date:"",
            // id:"",
          },
        ],
        pubItems:[
          {
            name:'1',    // 第几作者
            index:'',     //
            DOI:'',
            date:"",
            title:"",
            id:uniqueId(''),
          }
        ],
        awardItems:[
          {
            // name:'xxxx奖',
            // date:'xxxx.xx.xx',
            // id:uniqueId('to-do-'),
          }
        ]
        };
    },
    mounted(){
      var that = this;
      this.get_edu(that);
      this.get_pub(that);
      this.get_award(that);
    },
    methods: {
        get_edu (that){
          this.$http({
          url: '/get_edu/'
          })
          .then(function(response){
            var resp = JSON.stringify(response);
            var res = JSON.parse(resp)
            // console.log(res['data']['data'])
            for(let i = 0;i<=res['data']['data'].length;i++){
            that.eduItems.push({name:res['data']['data'][i]['fields'].my_edu_name ,major:res['data']['data'][i]['fields'].my_edu_major ,date:res['data']['data'][i]['fields'].my_edu_date ,degree:res['data']['data'][i]['fields'].my_edu_degree, id:uniqueId('to-do-')})
            }
            that.reload()
          },err=>{
            console.log(err);
            console.log("1jkjksdj")
          })
        },
        get_pub(that){
          this.$http({
            url: '/get_pub/'
          })
          .then(function(response){
            var resp = JSON.stringify(response);
            var res = JSON.parse(resp)
            // console.log(res['data']['data'])
            // console.log(res['data']['data'][0])

            for(let i = 0;i<=res['data']['data'].length;i++){
              console.log(res['data']['data'][i]['fields'].my_articles_name)
              console.log(res['data']['data'][i]['fields'].my_articles_DOI)
              that.pubItems.push({name:res['data']['data'][i]['fields'].my_articles_name ,DOI:res['data']['data'][i]['fields'].my_articles_DOI ,
              date:res['data']['data'][i]['fields'].my_articles_date,
              index:res['data']['data'][i]['fields'].my_articles_index ,
              title:res['data']['data'][i]['fields'].my_articles_title, 
              id:uniqueId('to-do-')})
            } 
            that.reload()
            },err=>{
            console.log(err);
            console.log("1jkjksdj")
          })
        },

        get_award(that){
          this.$http({
            url: '/get_award/'
        })
        .then(function(response){
            var resp = JSON.stringify(response);
            var res = JSON.parse(resp)
            // console.log(res['data']['data'])
            // console.log(typeof res['data']['data']);
            for(let i = 0;i<=res['data']['data'].length;i++){
            that.awardItems.push({name:res['data']['data'][i]['fields'].my_award_name ,date:res['data']['data'][i]['fields'].my_award_index, id:uniqueId('to-do-')})
            }
            that.reload()
          },err=>{
            console.log(err);
            console.log("1jkjksdj")
          })
        },
      },
    computed: {
      }
}
</script>

<style>
@import './assets/font/font.css';

*:before,
*:after {
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
}
  /* 全局样式 */
  html {
    font-size: 80.5%;
    font-family: 'JetBrainsMono-Regular', sans-serif;
    /* font-family: sans-serif; */
    -ms-text-size-adjust: 100%;
    display: block;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    -webkit-text-size-adjust: 100%;


}

  body {
    padding: 0;
    font-family: 'JetBrainsMono-Regular',sans-serif;
    background-color: white;
    height: 100%;
    font-size: 30px;
    line-height: 50px;
    /* font-family: 'Roboto', sans-serif; */
    text-align: justify;
    margin-left: 14%;
    margin-right: 12%;
    color: #333333;
    background-color: #ffffff;
}
div {
    display: block;
}
.container {
    max-width: 1400px;
    margin-right: auto;
    margin-left: -50px;
    line-height: 2.2;
    width:130%
}
.container .row {
    margin-right: 2px;
    margin-left: 0px; 
}
.page-header {
    border: none;
    margin-bottom: 0px;
}
.page-header h1 {
    font-size: 50px;
    margin-left: -120px;
}

.leftblock p {
    padding-top: 0px;
    margin-top: 8px;
    line-height: 16px;
}
.rightbar img {
    padding: 8px;
    border: 1px solid #CCCCCC;
    box-shadow: 2px 2px 3px #000;
}
.rightbar ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

.rightblock li {
    line-height: 20px;
    list-style-type: none;
}
div.rightblock {
    text-align: left;
    background-color: #d4d4d4;
    font-size: 15pt;
    margin-top: 1px;
    padding: 12px;
    padding-left: 10px;
    width: fit-content;
}
.page-header {
    border: none;
    margin-bottom: 0px;
    padding-bottom: 9px;
    margin: 40px 0 20px;
}
.leftbar {
    padding-right: 40px;
    border-right: #c0c0c0 dashed 1px;
}
.col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11 {
    float: left;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12, .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12, .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12, .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    position: relative;
    min-height: 1px;
    padding-right: 10px;
    padding-left: 10px;
}
a:hover,
a:focus {
  color: #2a6496;
  text-decoration: underline;
}
a:focus {
  outline: thin dotted #333;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
a.info {
    background: #D9EDF7;
    padding-left: 2px;
    padding-right: 2px;
}

div.title {
    padding-bottom: 15px;
}

img {
  vertical-align: middle;
}
.img-responsive {
  display: inline-block;
  height: auto;
  max-width: 100%;
}
.img-rounded {
  border-radius: 6px;
}

.img-circle {
  border-radius: 50%;
}


.col-sm-pull-3 {
    right: 26%;
}
.col-sm-push-9 {
    left: 76%;
}
.col-sm-9 {
    width: 90%;
}
.col-sm-3 {
    width: 10%;
}
.rightblock li {
    line-height: 16px;
    list-style-type: none;
}
p {
    width: 750px;
    margin: 0 0 10px;
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
}

ul {
    display: block;
    list-style-type: disc;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    padding-inline-start: 40px;
    margin-top: 0;
    margin-bottom: 10px;
}
li {
    display: list-item;
    text-align: -webkit-match-parent;
}
h1, h2, h3 {
    font-family: 'JetBrainsMono-Regular', sans-serif;
    margin-top: 50px;
    line-height: 1;
    /* text-transform: uppercase; */
    color: #990000;
    margin-bottom: 0px;
    font-weight: 700;
    text-align: left;
}
h3 {
    font-size: 26px;
}
h2 {
    font-size: 28px;
    padding-top: 8px;
    padding-bottom: 10px;
}
h1 {
  display: block;
    font-size: 2em;
    margin-block-start: 0.67em;
    margin-block-end: 0.67em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
}

h3 {
    display: block;
    /* font-size: 1.17em; */
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    /* font-weight: bold; */
}
</style>
