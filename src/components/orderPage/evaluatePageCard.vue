<!-- userOrderPage的子组件:展示该店铺的所有用户评价 -->

<!-- TODO:
1.展示本店铺的所有评价，实例化rateCard1，进行展示 -->

<template>
    <n-card class = "evaluateCardClass">
       <!--评价 -->
      <el-row class = "evaluateRow">
        <el-col :span="12" v-for="c in info.comments">
          <rateCard1 :comment="c"></rateCard1>
        </el-col>
      </el-row>
    </n-card>
</template>

<script setup>
import {defineProps, reactive, onMounted} from 'vue'
import {NCard} from 'naive-ui'
import {enter_comment} from "@/api/userMain";
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