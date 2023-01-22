<?php
/* Smarty version 4.2.1, created on 2023-01-22 04:12:37
  from '/var/www/html/amdin/themes/new-theme/template/footer.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '4.2.1',
  'unifunc' => 'content_63cca9a5536f69_59898035',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '552e54bd1b81c6a82f4c1b4d99b4868dc008cf83' => 
    array (
      0 => '/var/www/html/amdin/themes/new-theme/template/footer.tpl',
      1 => 1666787715,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_63cca9a5536f69_59898035 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="footer" class="bootstrap">
    <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['hook'][0], array( array('h'=>"displayBackOfficeFooter"),$_smarty_tpl ) );?>

</div>
<?php }
}
