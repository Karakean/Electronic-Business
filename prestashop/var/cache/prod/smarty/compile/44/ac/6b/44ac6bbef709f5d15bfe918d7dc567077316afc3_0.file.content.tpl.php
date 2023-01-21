<?php
/* Smarty version 4.2.1, created on 2023-01-21 15:30:59
  from '/var/www/html/amdin/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '4.2.1',
  'unifunc' => 'content_63cbf723ce4627_16189814',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '44ac6bbef709f5d15bfe918d7dc567077316afc3' => 
    array (
      0 => '/var/www/html/amdin/themes/new-theme/template/content.tpl',
      1 => 1666787715,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_63cbf723ce4627_16189814 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>
<div id="content-message-box"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
