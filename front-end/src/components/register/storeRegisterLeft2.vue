<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="storeRegisterLeft2" 
    >
      
        
  
      <el-form-item prop="address" class = "shopAddressInputBox">
        <el-input
          v-model="input"
          type="address"
          placeholder="店铺地址"
          size = "large"
          class = "shopAddressInputBoxClass"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><location /></el-icon>
          </template>
        </el-input>
  
      </el-form-item>

      <el-form-item prop="intro" class = "introInputBox">
        <el-input
            v-model="textarea2"
            :autosize="{ minRows: 3, maxRows: 4 }"
            type="textarea"
            placeholder="店铺介绍"
        >
        
        </el-input>
      </el-form-item>


      <el-form-item class = "storeLogo">
        <el-row class = "storeLogoRow">


          <el-col :span="12">
            <p class = "uploadLogoDetail">上传店铺头像</p>
           </el-col>


          <el-col :span="12">
            <el-upload
            class="avatar-uploader"
            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload"
            >
              <img v-if="imageUrl" :src="imageUrl" class="avatar" />
              <el-icon v-else class="logo-uploader-icon"><Plus /></el-icon>
            </el-upload>
          </el-col>


        </el-row>


        

      </el-form-item>

      
      <el-form-item class = "nextStepButton">
  
        <el-button 
          color = "#fec01b" 
          :dark="isDark" 
          round
          plain
          size = "large"
          class = "nextStepButton"  
        >
          提交申请
        </el-button>
  
      </el-form-item>

      
  
      <el-form-item class = "loginLink">
        
        <el-row class = "row">
        <el-col :span="12">  
            <el-link :underline="false">
            登录账号
          </el-link>
          </el-col>
        <el-col :span="12">
          <el-link :underline="false">
            返回首页
          </el-link>
        </el-col>
      </el-row>
          
      </el-form-item>
    </el-form>
  </template>
  
  <script lang="ts" setup>
  
  </script>
  
  <style scoped>
    .storeRegisterForm2 {
      width: 350px;
      height: 350px;
      border-radius: 20px;
      margin-top:0px;
      /* 整个表单el-form位于整个屏幕的位置 margin */ 
    }

    .shopNameInputBox {
      width: 300px;
      width: 300px;
      margin-top: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-bottom: 10px;
      height: 45px;
      
    }
    
    .shopAddressInputBox {
      width: 300px;
      width: 300px;
      margin-top: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-bottom: 10px;
      height: 45px;
      
    }


    .storeLogoRow {
      width: 300px;
    }
    
  
    .introInputBox {
      width: 300px;
      margin-bottom: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-top: 20px;
      height: 70px;
    }



    .nextStepButton {
      width: 300px;
      margin-top:2%;
      margin-left: auto;
      margin-right: auto;
      
    }
  
    .el-link {
      margin-right: 8px;
    }
    .el-link .el-icon--right.el-icon {
      vertical-align: text-bottom;
    }
  
    .loginLink {
      width: 300px;
      margin-left: 30%;
      padding: 0px 0px 0px auto;
      padding-left: 0px;
      /* border:2px solid black; */

      margin-bottom: 0px;
    }
  
    .row {
      width : 350px
    }

    .uploadLogoDetail {
      text-align: center;
      font-size: 15px;
      margin-left:20%;
      font-weight: bold;
      color:#606266;
    }

    .avatar-uploader .avatar {
    width: 178px;
    height: 178px;
    display: block;
    }

    .avatar-uploader .el-upload {
    border: 1px dashed var(--el-border-color);
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
  }
  
  .avatar-uploader .el-upload:hover {
    border-color: var(--el-color-primary);
  }
  
  .el-icon.logo-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 100px;
    height: 100px;
    text-align: center;
  }

  .storeLogo {
    margin-top :5%;
    margin-left:15%;
    width: 300px;
  }
  
  </style>