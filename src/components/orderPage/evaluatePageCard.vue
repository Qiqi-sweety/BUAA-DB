<!-- userOrderPage的子组件:展示该店铺的所有用户评价 -->

<template>
    <n-card class = "evaluateCardClass">
       <!--评价 -->
      <el-row class = "evaluateRow">
        <el-col :span="12" v-for="c in info.comments">
          <rateCard1 :comment="c"/>
        </el-col>
      </el-row>
    </n-card>
</template>

<script setup>
import {defineProps, reactive, onMounted} from 'vue'
import {NCard} from 'naive-ui'
import {enter_comment} from "@/api/user";
import {useRoute} from "vue-router";
const route = useRoute()

const info = reactive({
  comments: []
})
const props = defineProps({store_id: String})

onMounted(() => {
  enter_comment({
    store_id: route.query.store_id
  }).then(res => {
    let content = res.data
    console.log(content)
    info.comments = []
    if (content.code === "200") {
      content.comments.forEach(item => {
        info.comments.push(item)
      })
    }
  })
})

</script>

  <style>
  .evaluateCardClass {
    width: 95%;
    margin-bottom: 50px;
    margin-left: auto;
    margin-right: auto;
  }

  .evaluateRow {
    margin-left: 35px;
  }

</style>