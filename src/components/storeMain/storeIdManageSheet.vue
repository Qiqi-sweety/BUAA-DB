<!-- storeMainPage的子组件：账号设置组件 -->

<!-- TODO：
1.展示该店铺的信息：头像，店铺名，地址，介绍，密码，营业执照
2.点击修改按钮可以修改店铺的信息 -->

<template>

    <NCard style = "width:1390px;margin-left:30px">
      <h3 style = "font-size: 30px;margin-top: 0%;margin-left:20px">账号设置</h3>
      <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 150px;">头像</p>
          </el-col>
          <el-col :span="1">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>

          <el-col :span="11">
            <img :src="{logoUrl}" style = "width: 85px;height: 85px;">
          </el-col>
          <el-col :span="6">
            <n-upload
            action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"
            @before-upload="beforeUpload"
            >
              <n-button type="warning" size = "large" round 
              style = "width: 100px;margin-left:100px;margin-top: 25px;"
              >
                修改
              </n-button>
            </n-upload>            
          </el-col>
        </el-row>
      <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 130px;">店铺名</p>
          </el-col>
          <el-col :span="1">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>
          <el-col :span="11">
            <p 
            style = "font-size:20px;color:gray;margin-top: 30px;">
              {{storeName}}
            </p>
          </el-col>

          <el-col :span="6">
            <n-button type="warning" size = "large" round 
            style = "width: 100px;margin-left:100px;margin-top: 25px;"
            @click="showIdModal = true">
            修改
            </n-button>
          </el-col>
        </el-row>
      <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 150px;">地址</p>
          </el-col>
          <el-col :span="1">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>
          <el-col :span="11">
            <p 
            style = "font-size:20px;color:gray;margin-top: 30px;">
              {{address}}
            </p>
          </el-col>

          <el-col :span="6">
            <n-button type="warning" size = "large" round 
            style = "width: 100px;margin-left:100px;margin-top: 25px;"
            @click="showAddressModal = true">
            修改
            </n-button>
          </el-col>
        </el-row>
      <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 150px;">介绍</p>
          </el-col>
          <el-col :span="1">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>
          <el-col :span="11">
            <p 
            style = "font-size:20px;color:gray;margin-top: 30px;">
            {{intro}}
            </p>
          </el-col>

          <el-col :span="6">
            <n-button type="warning" size = "large" round 
            style = "width: 100px;margin-left:100px;margin-top: 25px;"
            @click="showIntroModal = true"
            >
            修改
            </n-button>
          </el-col>
        </el-row>
      <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 150px;">密码</p>
          </el-col>
          <el-col :span="6">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>
          <el-col :span="6"></el-col>

          <el-col :span="6">
            <n-button type="warning" size = "large" round 
            style = "width: 100px;margin-left:100px;margin-top: 25px;"
            @click="showPasswordModal = true"
            >
            修改
            </n-button>
          </el-col>
        </el-row>
        <el-divider/>
        <el-row>
          <el-col :span="6">
            <p style = "font-size: 25px;margin-left: 100px;">营业执照</p>
          </el-col>
          <el-col :span="1">
            <el-divider direction="vertical" style="height:80px;margin-top:10px"/>
          </el-col>
          <el-col :span="11">
            <img :src="{licenseUrl}" style = "width: 150px;height: 100px;">
          </el-col>
          <el-col :span="6">
            <n-upload
            action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"
            @before-upload="beforeUpload"
            >
              <n-button type="warning" size = "large" round 
              style = "width: 100px;margin-left:100px;margin-top: 25px;"
              >
                修改
              </n-button>
            </n-upload>            
          </el-col>
        </el-row>
    </NCard>

    <n-modal
    v-model:show="showIdModal"
    preset="card"
    :style="bodyStyle"
    title="修改用户名"
    style="width:400px;height:250px"
    :bordered="false"
    :segmented="segmented"
    >
        <n-card
        style="width: 350px"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
        >
        <el-input
          v-model="input"
          type="name"
          size = "large"
          placeholder="请输入新用户名"
          style = "margin-bottom: 40px;"
        >
        
          <template #prefix>
            <el-icon class="el-input__icon"><user /></el-icon>
          </template>
        </el-input>
        <n-button style = "margin-left:80px;" size = "large" round type="warning">
        确认修改
        </n-button>  
    </n-card>
  </n-modal>

  <n-modal
    v-model:show="showAddressModal"
    preset="card"
    :style="bodyStyle"
    title="修改地址"
    style="width:400px;height:250px"
    :bordered="false"
    :segmented="segmented"
    >
        <n-card
        style="width: 350px"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
        >
        <el-input
          v-model="input"
          type="name"
          size = "large"
          placeholder="请输入新地址"
          style = "margin-bottom: 40px;"
        >
        
          <template #prefix>
            <el-icon class="el-input__icon"><position /></el-icon>
          </template>
        </el-input>
        <n-button style = "margin-left:80px;" size = "large" round type="warning">
        确认修改
        </n-button>  
    </n-card>
  </n-modal>

  <n-modal
    v-model:show="showIntroModal"
    preset="card"
    :style="bodyStyle"
    title="修改介绍"
    style="width:500px;height:400px"
    :bordered="false"
    :segmented="segmented"
    >
        <n-card
        style="width: 450px"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
        >
        <n-input
        v-model:value="value"
        type="textarea"
        placeholder="请输入新的店铺介绍"
        style = "height: 200px;"
        />
        
        <n-button style = "margin-left:130px;margin-top: 25px;" size = "large" round type="warning">
        确认修改
        </n-button>  
    </n-card>
  </n-modal>

  <n-modal
    v-model:show="showPasswordModal"
    preset="card"
    :style="bodyStyle"
    title="修改密码"
    style="width:400px"
    :bordered="false"
    :segmented="segmented"
    >
        <n-card
        style="width: 350px"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
        >

       
        <el-input
          v-model="input"
          type="password"
          placeholder="设置新密码"
          show-password
          size = "large"
          style = "margin-bottom: 20px;" 
        >
          <template #prefix>
            <el-icon class="el-input__icon"><lock /></el-icon>
          </template>
  
        </el-input>

        <el-input
          v-model="input"
          type="password"
          placeholder="确认新密码"
          show-password
          size = "large"
          style = "margin-bottom: 30px;" 
        >
          <template #prefix>
            <el-icon class="el-input__icon"><lock /></el-icon>
          </template>
  
        </el-input>
  
        <n-button style = "margin-left:80px;" size = "large" round type="warning">
        确认修改
        </n-button>  
    </n-card>
  </n-modal>


</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import {NCard,NRate,NButton,NModal,NUpload,NInput} from 'naive-ui'

  export default defineComponent({
    components: {
      NCard,
      NRate,
      NButton,
      NModal,
      NUpload,
      NInput,
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
      intro:{
        type:String
      },
      licenseUrl:{
        type:String

      }
    },
    setup() {
    return {
      showIdModal: ref(false),
      showAddressModal: ref(false),
      showIntroModal: ref(false),
      showPasswordModal: ref(false),
      value: ref(null)
    };
    }

  })
  </script>