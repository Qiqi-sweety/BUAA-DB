<!-- 位于用户个人中的我的评价中的用户评价卡 -->
<template>
    <NCard style = "width: 680px;height: 450px;">
        <el-row>
            <el-col :span="6">
<!--              user_logo-->
              <img src="../../assets/card.jpg"
                style = "width: 100px;height: 100px;background-color: white;">
            </el-col>
            <el-col :span="14">
                <h3 style = "font-size: 25px;margin-bottom: 10px;">
                  {{props.comment.user_name}}
                </h3>
            </el-col>
            <el-col :span="4">
                <p style = "margin-top: 20px;color: gray;">
                  日期：{{props.comment.time}}
                </p>
            </el-col>
        </el-row>

        <el-row>
            <el-col :span="14">
              <el-rate disabled v-model="props.comment.star" style = "margin-left: 20px;" size = "large"/>
                <h3 style = "font-size: 17px;margin-left: 20px;margin-right: 20px;">
                {{props.comment.content}}
                </h3>
            </el-col>
            <el-col :span="10">
              <img v-if="props.comment.image" :src="`/api${props.comment.image}`" style = "margin-top: 0%;width: 240px;height: 290px;">
            </el-col>
        </el-row>
    </NCard>
</template>

<script setup>
import {NCard} from 'naive-ui'
const props = defineProps({
  comment: Object
})
</script>