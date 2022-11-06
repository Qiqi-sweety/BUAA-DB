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
                {{address}}    
                </p>
                <p class = "homePageWord">
                {{intro}}    
                </p>
            </el-col>
            <el-col :span="8">
                <img :src="{logoUrl}" class = "homePageImageClass">
            </el-col>
        </el-row>
    </NCard>
    <h3 class = "recommendTitle">推荐菜</h3>
    <NCard class = "recommendCardClass">
        <el-row style = "margin-left:60px;">
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
      logoUrl:{
        type:String
      },
      storeName:{
        type:String
      },
      address:{
        type:String
      },
      star:{
        type:Number
      },
      number:{
        type:Number
      },
      intro:{
        type:String
      }
    },
  })
</script>

<style>
.introCardClass {
 width: 95%;
 /* height: 100px; */
 margin-left: auto;
 margin-right: auto;
}

.recommendCardClass {
 width: 95%;
 margin-top: 20px;
 margin-left: auto;
 margin-right:auto;
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
</style>