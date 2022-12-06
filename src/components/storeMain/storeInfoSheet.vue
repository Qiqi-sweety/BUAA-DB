<template>
    <NCard class = "introCardClass">
        <el-row>
            <el-col :span="16">
                <h3 class = "homePageName">{{info.store.name}}</h3>
                <el-row>
                    <el-col :span="12">
                        <el-rate disabled
                                v-model="info.store.star"
                                class = "homePageRateClass"
                                size = "large">
                        </el-rate>
                    </el-col>
                    <el-col :span="12">
                        <p class = "homePageNumber">销量：{{info.store.sales}}</p>
                    </el-col>
                </el-row>
                <el-divider />
                <p class = "homePageWord">{{info.store.address}}</p>
                <p class = "homePageWord">{{info.store.info}}</p>
            </el-col>
            <el-col :span="8">
                <img :src="`/api${info.store.logo}`" class = "homePageImageClass">
            </el-col>
        </el-row>
    </NCard>
    <h3 class = "recommendTitle">推荐菜</h3>
    <NCard class = "recommendCardClass">
        <el-row style = "margin-left:60px;">
            <el-col :span="6" v-for="item in info.items">
              <foodCard2 :item="item" :store_id="info.store.id"/>
            </el-col>
        </el-row>
    </NCard>

</template>

<script setup>
import {NCard} from "naive-ui"
import {onMounted, reactive} from "vue";
import {store_homepage} from "@/api/store";
import {ElMessage} from "element-plus";

const info = reactive({
  store: {},
  items: []
})

onMounted(() => {
  store_homepage().then(res => {
    let content = res.data
    console.log(content)
    if (content.code === "200") {
      info.store = content.store_data
      content.item_data.forEach(item => {
        info.items.push(item)
      })
    } else {
      ElMessage({message: content.message, type: "error"})
    }
  })
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