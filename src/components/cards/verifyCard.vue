<template>
    <n-card style = "width: 700px;height: 400px;">
        <el-row>
            <el-col :span="16">
                <el-row style = "margin-bottom: 0%;">
                    <el-col :span="6">
                        <h3 style = "font-size: 20px;">店铺头像：</h3>
                    </el-col>
                    <el-col :span="18">
                        <img :src="{logoUrl}" style = "width: 80px;height: 80px;">
                    </el-col>
                    
                </el-row>
                <el-row style = "margin-top: 0%;margin-bottom: 0%;">
                    <el-col :span="6"><h3 style = "font-size: 20px;">店铺名：</h3></el-col>
                    <el-col :span="18"><p style = "font-size: 20px;">{{name}}</p></el-col>
                </el-row>
                <el-row style = "margin-top: 0%;margin-bottom: 0%;">
                    <el-col :span="6"><h3 style = "font-size: 20px;">店铺地址：</h3></el-col>
                    <el-col :span="18"><p style = "font-size: 20px;">{{address}}</p></el-col>
                </el-row>
                <el-row style = "margin-top: 0%;margin-bottom: 0%;">
                    <el-col :span="6"><h3 style = "font-size: 20px;">店铺介绍：</h3></el-col>
                    <el-col :span="18"><p style = "font-size: 20px;">{{intro}}</p></el-col>
                </el-row>
            
            </el-col>
            <el-col :span="8">
                <img :src="{licenseUrl}" style = "width: 220px;height: 150px;">
                <n-button size = "large" round type="warning" style = "margin-top: 100px;margin-left: 80px;">
                审核通过
                </n-button>
            </el-col>
        </el-row>

    </n-card>
</template>

<script>
import { defineComponent ,ref } from 'vue'
import { NCard,NButton} from 'naive-ui'
export default defineComponent({
  name: 'foodCard1',
  components: {
    NCard,
    NButton,
  },
  props:{
    logoUrl:{
        type:String
    },
    licenseUrl:{
        type:String
    },
    name:{
        type:String
    },
    address:{
        type:String
    },
    intro:{
        type:String
    }

  }
})
</script>