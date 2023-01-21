<?php
/* Smarty version 4.2.1, created on 2023-01-21 15:30:15
  from '/var/www/html/amdin/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '4.2.1',
  'unifunc' => 'content_63cbf6f7d71199_90311247',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '8ee9afc2cf9250b2592ea2b40f4d2f119ba8ce82' => 
    array (
      0 => '/var/www/html/amdin/themes/default/template/content.tpl',
      1 => 1666787715,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_63cbf6f7d71199_90311247 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>
<div id="content-message-box"></div>

<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
	<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
