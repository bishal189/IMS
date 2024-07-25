$(document).ready(function () {
    function loadCurrentSystemDate() {
        var currentDate = new Date();
        var year = currentDate.getFullYear();
        var month = String(currentDate.getMonth() + 1).padStart(2, '0');
        var day = String(currentDate.getDate()).padStart(2, '0');
        var formattedDate = `${year}-${month}-${day}`;

        document.getElementsByName('invoice_date')[0].value = formattedDate;
    }

    function calcRow(row) {
        var qty = parseFloat(row.find('.qty').val()) || 0;
        var price = parseFloat(row.find('.price').val()) || 0;
        var rowTotal = qty * price;

        var discountInput = row.find('.discount').val();
        var discountVal = calculateDiscount(discountInput, rowTotal);

        var totalAfterDiscount = rowTotal - discountVal;

        var vatInput = row.find('.vat').val();
        var vatVal = calculateVAT(vatInput, totalAfterDiscount);

        var grandTotal = totalAfterDiscount + vatVal;

        row.find('.total').val(grandTotal.toFixed(2));
        row.find('.sub_total').val(rowTotal.toFixed(2));
        row.find('.total_discount').val(discountVal.toFixed(2));
        row.find('.tax_amount').val(totalAfterDiscount.toFixed(2));
        row.find('.total_vat').val(vatVal.toFixed(2));
        row.find('.total_amount').val(grandTotal.toFixed(2));

        // Calculate and display totals
        calculateTotals();
    }

    function calculateVAT(vatInput, total) {
        var vat = parseFloat(vatInput) || 0;
        return vatInput.includes('%') ? total * (vat / 100) : vat;
    }

    function calculateDiscount(discountInput, total) {
        var discount = parseFloat(discountInput) || 0;
        return discountInput.includes('%') ? total * (discount / 100) : discount;
    }

    function calculateTotals() {
        var subTotal = 0;
        var totalDiscount = 0;
        var taxAmount = 0;
        var totalVAT = 0;

        $('.addr').each(function () {
            var row = $(this);
            var rowTotal = parseFloat(row.find('.total').val()) || 0;
            var discount = parseFloat(row.find('.total_discount').val()) || 0;
            var vat = parseFloat(row.find('.total_vat').val()) || 0;

            subTotal += rowTotal;
            totalDiscount += discount;
            taxAmount += rowTotal - discount;
            totalVAT += vat;
        });

        $('#sub_total').val(subTotal.toFixed(2));
        $('#total_discount').val(totalDiscount.toFixed(2));
        $('#tax_amount').val(taxAmount.toFixed(2));
        $('#total_vat').val(totalVAT.toFixed(2));
    }


    function calculateAllRows() {
        // Calculate and update totals for initial rows
        $('#tab_logic tbody tr').each(function () {
            calcRow($(this));
        });

        // Calculate and update totals for dynamic rows
        $('.addr').each(function () {
            calcRow($(this));
        });

        // Calculate and display totals
        calculateTotals();
    }

    loadCurrentSystemDate();

    var i = 1;
    $("#add_row").click(function () {
        var newRow = `<tr class="addr${i}">
        <td><input type="checkbox" class="select_row"></td>
        <td>${i + 1}</td>
        <td><input list="products" placeholder="Product Name" name="product_${i}" id="product_${i}" class="form-control form-control-sm product input-field">
        <datalist id="products" style="width: 395px;"></datalist></td>
        <td><input type="number" name="qty_${i}" class="form-control form-control-sm qty input-field" placeholder="0.00" step="0" min="0"/></td>
        <td><select name="unit_${i}" class="form-control form-control-sm unit input-field"><option value="kg">kg</option><option value="lbs">lbs</option><option value="pcs">pcs</option></select></td>
        <td><input type="number" name="price_${i}" class="form-control form-control-sm price input-field" placeholder="0.00" step="0.00" min="0"/></td>
        <td><input type="text" name="discount_${i}" class="form-control form-control-sm discount input-field" placeholder="0.00" /></td>
        <td><input type="text" name="vat_${i}" class="form-control form-control-sm vat input-field" placeholder="0.00" step="0.00" min="0"/></td>
        <td><input type="number" name="total_${i}" class="form-control form-control-sm total total-input" readonly/></td>
    </tr>`;

    $('#tab_logic').append(newRow);
    i++;

    // Move focus to the first input of the newly added row
    $('#product_' + i).focus();
        // ... (existing code)

        // Calculate and display totals
        calculateAllRows();
    });


    $('#tab_logic').on('change', '.select_row', function () {
        // ... (existing code)
        handleRowSelection($(this).closest('tr'));

        // Calculate and display totals
        calculateTotals();
    });


    $(document).on('click', '#delete_row', function () {
        // ... (existing code)
        $(".select_row:checked").each(function () {
            $(this).closest('tr').remove();
        });

        // Calculate and display totals
        calculateTotals();
    });

    $('#tab_logic tbody').on('input', 'input, select', function () {
        calcRow($(this).closest('tr'));
    });


    $('#tab_logic tbody').on('keyup', 'input', function (e) {
        // ... (existing code)
        if (e.which == 13) {
            var $inputs = $(this).closest('tr').find(':input');
            var idx = $inputs.index(this);
            if (idx == $inputs.length - 1) {
                $("#add_row").click();
            } else {
                $inputs.eq(idx + 1).focus();
            }
        }

        // Calculate and display totals
        calculateTotals();
    });

    $(".btn-primary").click(function () {
        setTimeout(function () {
            console.log("Save operation completed");
        }, 3000);
    });

    // Keyboard shortcuts
    $(document).keydown(function (e) {
        // ... (existing code)
        

        switch (e.which) {
            case 88: // Alt + X for selecting a row
            case 90: // Alt + Z for deleting selected rows
                calculateAllRows(); // Recalculate totals after row selection or deletion
                break;

            default:
                break;
        }
    });
});
