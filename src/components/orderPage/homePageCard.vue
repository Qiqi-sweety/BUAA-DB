<!-- userOrderPage的子组件：店铺首页的卡片 -->

<!-- 用于展示商家的信息给顾客看 -->
<template>
    <NCard class = "introCardClass">
        <el-row>
            <el-col :span="16">
                <h3 class = "homePageName">{{storeName}}</h3>
                <el-row>
                    <el-col :span="12">
                        <n-rate allow-half readonly :default-value={star} class = "homePageRateClass" size = "large">        
                        </n-rate>
                    </el-col>
                    <el-col :span="12">
                        <p class = "homePageNumber">销量：{{number}}</p>
                    </el-col>
                </el-row>
                <el-divider />
                <p class = "homePageWord">
                    地址：{{address}} 
                </p>
                <p class = "homePageWord">
                介绍：{{intro}}
                </p>


            </el-col>
            <el-col :span="8">
                <img :src="{logoUrl}" class = "homePageImageClass">
            </el-col>
        </el-row>
    </NCard>
    <h3 class = "recommendTitle">推荐菜</h3>
    <NCard
    style = " width: 95%;
            margin-top: 20px;
            margin-left: auto;
            margin-right:auto;">
        <el-row class = "recommendCardRow">
            <el-col :span="6"><foodCard2/></el-col>
            <el-col :span="6"><foodCard2/></el-col>
            <el-col :span="6"><foodCard2/></el-col>
            <el-col :span="6"><foodCard2/></el-col>
        </el-row>
    </NCard>

</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NCard,NRate} from 'naive-ui'
  import foodCard2 from "../cards/foodCard2.vue"

  export default defineComponent({
    components: {
      NCard,
      NRate,
      foodCard2,
    },
    props:{
        storeName:{
            type:String
        },
        star:{
            type:Number
        },
        number:{
            type:Number
        },
        address:{
            type:String
        },
        intro:{
            type:String
        },
        logoUrl:{
            type:String
        }
    }
  })
</script>

<style>
.introCardClass {
 width: 95%;
 /* height: 100px; */
 margin-left: auto;
 margin-right: auto;
}


.homePageImageClass {
    margin-top: 50px;
    width: 450px;
    height: 450px;
}

.homePageName {
    margin-left: 100px;
    margin-bottom: 0%;
    font-size: 40px;
}

.homePageRateClass {
    margin-left: 100px;
    margin-top: 20px;
}

.homePageWord {
    font-size: 20px;
    color: gray;
    margin-left: 100px;
    margin-right: 20px;
}

.homePageNumber {
    font-size: 20px;
    color: gray;
}

.recommendTitle {
    margin-left: 50px;
    font-size: 25px;
    margin-top:20px;
    margin-bottom: 0px;
}

.recommendCardRow {
    margin-left:60px;
}


</style>