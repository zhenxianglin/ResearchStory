/*----------------------------自定义timepicker控件-----------------------*/
(function ($) {
    var tpk = (function(){
        return {
            // 唤起timepicker控件
            tpkArouse: function (e) {
                if ($(e.target).next().length > 0 && $(e.target).next().hasClass('tpkwrapper')) {
                    $(e.target).next().fadeIn().find('.tpk-hour input').trigger('focus');
                    return;
                }
                var _flex = '<a href="javascript:void(0)" class="adjuster adjuster-up" tabindex="-1"><i class="glyphicon glyphicon-chevron-up"></i></a>' +
                        '<input type="number" class="form-control input-sm" min="0" max="$max$" />' +
                        '<a href="javascript:void(0)" class="adjuster adjuster-down" tabindex="-1"><i class="glyphicon glyphicon-chevron-down"></i></a>';
                var _html = '<div class="tpkwrapper"> <div class="tpk-arrow"></div>' +
                '<div class="tpk-body">' +
                        '<div data-cg="hour" class="tpk-hour">' + _flex.replace('$max$', '23') + '</div>' +
                        '<div class="tpk-slit">:</div>' +
                        '<div data-cg="min" class="tpk-min">' + _flex.replace('$max$', '59') + '</div>' +
                        '<div class="tpk-slit">:</div>' +
                        '<div data-cg="sec" class="tpk-sec">' + _flex.replace('$max$', '59') + '</div>' +
                 '</div>' +
                 '</div>';
                var $box = $(_html);
                var top = e.target.offsetTop + e.target.offsetHeight + 6;
                var left = e.target.offsetLeft;
                $box.data('trigger', e.target)
                    .data('top', top).data('left', left)
                    .css({ 'top': top, 'left': left, opacity: 1 })
                    .on('click', '.adjuster', tpk.tpkAdjust);
                $box.find('.tpk-body input').on('change', function (e) {
                    tpk.timePickerSet(e.target, $(e.target).val(), true);
                    return false;
                });

                var val = e.target.value;
                if (!!val) {
                    var arr = val.split(':');
                    if (arr.length > 0) {
                        tpk.timePickerSet($box.find('.tpk-hour input'), arr[0], false);
                        if (arr.length > 1) {
                            tpk.timePickerSet($box.find('.tpk-min input'), arr[1], false);
                            if (arr.length > 2) {
                                tpk.timePickerSet($box.find('.tpk-sec input'), arr[2], false);
                            } else {
                                tpk.timePickerSet($box.find('.tpk-sec input'), 0, false);
                            }
                        } else {
                            tpk.timePickerSet($box.find('.tpk-min input'), 0, false);
                            tpk.timePickerSet($box.find('.tpk-sec input'), 0, false);
                        }
                    } else {
                        tpk.timePickerSet($box.find('.tpk-hour input'), 0, false);
                        tpk.timePickerSet($box.find('.tpk-min input'), 0, false);
                        tpk.timePickerSet($box.find('.tpk-sec input'), 0, false);
                    }
                } else {
                    tpk.timePickerSet($box.find('.tpk-hour input'), 0, false);
                    tpk.timePickerSet($box.find('.tpk-min input'), 0, false);
                    tpk.timePickerSet($box.find('.tpk-sec input'), 0, false);
                }

                $(e.target).after($box);
                // show picker
                $box.fadeIn()
                    .find('.tpk-hour input').trigger('focus');

                $(document).on('mousedown keyup', function (e) {
                    // Clicked outside the tpkwrapper, hide picker
                    if ($(e.target).closest('.tpkwrapper').length === 0) {
                        $box.fadeOut();
                    }
                });
            },
            // 点击按钮调整timepicker控件值
            tpkAdjust: function (e) {
				let $adjuster = $(e.target).closest('.adjuster');
                var add = $adjuster.hasClass('adjuster-up');
				let num = $adjuster.hasClass('adjuster-up')? (Number($adjuster.next().val()) + 1):(Number($adjuster.prev().val()) - 1);
                // var num = Number($adjuster.parent().find('input').val());
                // if (add) { num++; } else { num--; }
                var fun = $adjuster.parent().data('cg');
                tpk.timePickerSet($adjuster.parents('.tpk-body').find('.tpk-'+ fun +' input'), num, true);
            },
            // 设置timepicker控件值，通过f参数设置是否更新到唤起timepicker控件的元素值
            timePickerSet: function (target, num, f) {
                num = Number(num);
                if (isNaN(num)) { return; }
                var max = Number($(target).prop('max'));
                if (num <= 0) {
                    num = 0;
                    $(target).next().prop('disabled', true).addClass('disabled');
                } else {
                    $(target).next().prop('disabled', false).removeAttr('disabled').removeClass('disabled');
                }
                if (num >= max) {
                    $(target).prev().prop('disabled', true).addClass('disabled');
                    num = max;
                } else {
                    $(target).prev().prop('disabled', false).removeAttr('disabled').removeClass('disabled');
                }
                if (num < 10) { num = '0' + String(num); }
                $(target).val(num);
                if (f) {
                    var time = [];
                    var $inputs = $(target).parents('.tpk-body').find('input');
                    for (var i = 0; i < 3; i++) {
                        time[i] = $($inputs[i]).val();
                        if (time[i].length === 1) {
                            time[i] = '0' + time[i];
                            $($inputs[i]).val(time[i]);
                        }
                    }
                    $($(target).parents('.tpkwrapper').data('trigger')).val(time.join(':'));
                }
            }
        };
    })();	
    $.fn.extend({
        timePicker:function(){
            $(this).on('click',tpk.tpkArouse);
        }
    });
})(jQuery);